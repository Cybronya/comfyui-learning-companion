# BreezeTTS2MultiSpeaker

## 节点类型

`BreezeTTS2MultiSpeaker`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `breeze_model:BREEZE_TTS2_MODEL`（10 次）
- `speaker_1:BREEZE_SPEAKER`（10 次）
- `speaker_2:BREEZE_SPEAKER`（10 次）
- `speaker_3:BREEZE_SPEAKER`（10 次）
- `speaker_4:BREEZE_SPEAKER`（10 次）
- `speaker_5:BREEZE_SPEAKER`（10 次）
- `speaker_6:BREEZE_SPEAKER`（10 次）
- `speaker_7:BREEZE_SPEAKER`（10 次）
- `speaker_8:BREEZE_SPEAKER`（10 次）
- `text:STRING`（10 次）

## 输出

- `audio:AUDIO`（10 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["小雨: 你们看这张，昨天晚上 10 点拍的，居然比白天的还好看。\n阿杰: [笑] 你确定？我怎么觉得我在里面像个路人。\n安安: 哈哈，你本来就是路人啊。对了，小雨，你把照片发给我，我想拿这张发到 YouTube，顺便 @一下昨天给我`（6 次）
- `["[\n  {\"speaker\": \"系统\", \"text\": \"冰冷的金属音毫无起伏，回荡在白色处置室。\"},\n  {\"speaker\": \"系统\", \"text\": \"公民凯恩，编号七三四‑F九一。经职`（3 次）
- `["Alice: Hey Bob, did you finish recording the demo?\nBob: (sigh) Almost. I just need one more take.\nAlice: (laugh) Tha`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
