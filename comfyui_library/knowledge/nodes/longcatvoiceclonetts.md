# LongCatVoiceCloneTTS

## 节点类型

`LongCatVoiceCloneTTS`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `prompt_audio:AUDIO`（4 次）
- `model_path:COMBO`（4 次）
- `text:STRING`（4 次）
- `prompt_text:STRING`（4 次）
- `steps:INT`（4 次）
- `guidance_strength:FLOAT`（4 次）
- `guidance_method:COMBO`（4 次）
- `device:COMBO`（4 次）
- `dtype:COMBO`（4 次）
- `attention:COMBO`（4 次）

## 输出

- `audio:AUDIO`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["LongCat-AudioDiT-3.5B-bf16", "太阳在晴朗的蓝天中明亮地照耀，微风轻轻吹拂，鸟儿唱着悦耳的旋律，世界充满了等待探索的美丽和奇迹", "Want to level up your Python skills? `（1 次）
- `["LongCat-AudioDiT-1B", "", "经常有小伙伴们夸赞我好温柔，说我简直就是一个温柔大姐姐。你们知道吗？在我没有做博主接受到这些评论的信息之前，我从来没有思考过，也没有意识到过自己是温柔与否这件事情。", 16, 4,`（1 次）
- `["LongCat-AudioDiT-3.5B-fp8", "太阳在晴朗的蓝天中明亮地照耀，微风轻轻吹拂，鸟儿唱着悦耳的旋律，世界充满了等待探索的美丽和奇迹", "", 15, 4, "apg", "auto", "auto", "sage`（1 次）
- `["LongCat-AudioDiT-3.5B-fp8", "我是由AI自动化视频生成系统生成的，它可以实现常文案的口播，也可以做音乐mv视频！", "经常有小伙伴们夸赞我好温柔，说我简直就是一个温柔大姐姐。你们知道吗？在我没有做博主接受到`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
