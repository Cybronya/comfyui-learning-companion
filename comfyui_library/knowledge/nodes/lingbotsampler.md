# LingBotSampler

## 节点类型

`LingBotSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `lingbot_model:LINGBOT_MODEL`（2 次）
- `embeds:LINGBOT_EMBEDS`（2 次）
- `image:IMAGE`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `num_frames:INT`（2 次）
- `steps:INT`（2 次）
- `guidance:FLOAT`（2 次）
- `shift:FLOAT`（2 次）
- `seed:INT`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[480, 480, 81, 20, 3, 3, 592466700376590, "fixed", "yes (low VRAM)", "off (stable colors, needs ~6GB free at decode)"]`（1 次）
- `[480, 480, 81, 20, 3, 3, 101056473802031, "randomize", "yes (low VRAM)", "on (lowest VRAM, can drift color/exposure)"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
