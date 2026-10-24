# PhysicEditSampler

## 节点类型

`PhysicEditSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `pipe:PhysicEditPipe`（5 次）
- `edit_image:IMAGE`（5 次）
- `prompt:STRING`（5 次）
- `num_inference_steps:INT`（5 次）
- `seed:INT`（5 次）

## 输出

- `image:IMAGE`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["改为双手比耶", 40, 40, "randomize"]`（1 次）
- `["改为拿起咖啡杯不小心咖啡溅到手机上", 40, 1128, "randomize"]`（1 次）
- `["打水漂，一颗非常小的石头在水上弹了1下", 12, 1837, "randomize"]`（1 次）
- `["让一个8岁的中国小学生穿上这件套装，人物站在画面的正中央，背景是：站在晴朗的蓝色天空下的操场上。隐约能看到学校，是一所小学。", 40, 1067, "randomize"]`（1 次）
- `["", 40, 417, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
