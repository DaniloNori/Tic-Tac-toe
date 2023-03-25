#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QMessageBox>
#include <QLineEdit>

class TicTacToe : public QWidget {
public:
    TicTacToe(QWidget* parent = nullptr);
private:
    void initializeUi();
    void disableButtons(const QList<QPushButton*>& buttons);
    void handleClick(QPushButton* button, QList<QPushButton*>& buttons);
    void checkForWin(const QList<QPushButton*>& buttons);
private:
    QLineEdit* m_player1Name = nullptr;
    QLineEdit* m_player2Name = nullptr;
    QString m_player1 = "";
    QString m_player2 = "";
    bool m_isPlayer1 = true;
    int m_turns = 0;
    QList<QPushButton*> m_buttons;
};

TicTacToe::TicTacToe(QWidget* parent)
    : QWidget(parent)
{
    initializeUi();
}

void TicTacToe::initializeUi() {
    setWindowTitle("Tic Tac Toe");

    QLabel* label1 = new QLabel("Player 1:", this);
    label1->setFont(QFont("Times", 20, QFont::Bold));
    label1->setGeometry(0, 0, 200, 50);

    m_player1Name = new QLineEdit(this);
    m_player1Name->setGeometry(100, 0, 200, 50);

    QLabel* label2 = new QLabel("Player 2:", this);
    label2->setFont(QFont("Times", 20, QFont::Bold));
    label2->setGeometry(0, 50, 200, 50);

    m_player2Name = new QLineEdit(this);
    m_player2Name->setGeometry(100, 50, 200, 50);

    QPushButton* resetButton = new QPushButton("Reset", this);
    resetButton->setGeometry(150, 100, 100, 50);
    connect(resetButton, &QPushButton::clicked, [this]() {
        m_isPlayer1 = true;
        m_turns = 0;
        m_player1Name->setEnabled(true);
        m_player2Name->setEnabled(true);
        for (auto button : m_buttons) {
            button->setText("");
            button->setEnabled(true);
        }
    });

    int x = 0;
    int y = 150;
    for (int i = 0; i < 9; i++) {
        QPushButton* button = new QPushButton(this);
        button->setGeometry(x, y, 50, 50);
        m_buttons.push_back(button);
        connect(button, &QPushButton::clicked, [this, button]() {
            handleClick(button, m_buttons);
        });

        x += 50;
        if ((i + 1) % 3 == 0) {
            x = 0;
            y += 50;
        }
    }
}

void TicTacToe::disableButtons(const QList<QPushButton*>& buttons) {
    for (auto button : buttons) {
        button->setEnabled(false);
    }
}

void TicTacToe::handleClick(QPushButton* button, QList<Q