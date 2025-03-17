eval 'set +o history' 2>/dev/null || setopt HIST_IGNORE_SPACE 2>/dev/null
 touch ~/.gitcookies
 chmod 0600 ~/.gitcookies

 git config --global http.cookiefile ~/.gitcookies

 tr , \\t <<\__END__ >>~/.gitcookies
chromium.googlesource.com,FALSE,/,TRUE,2147483647,o,git-macwater90.gmail.com=1//03XQbj9xHI8zcCgYIARAAGAMSNwF-L9IrOm2_F__qdfTGHXfCwClC1YGZQwBFLtkYk1ol9aCiNzV6rNqHd1c5EXHyTdN5DbMIeTo
chromium-review.googlesource.com,FALSE,/,TRUE,2147483647,o,git-macwater90.gmail.com=1//03XQbj9xHI8zcCgYIARAAGAMSNwF-L9IrOm2_F__qdfTGHXfCwClC1YGZQwBFLtkYk1ol9aCiNzV6rNqHd1c5EXHyTdN5DbMIeTo
__END__
eval 'set -o history' 2>/dev/null || unsetopt HIST_IGNORE_SPACE 2>/dev/null
