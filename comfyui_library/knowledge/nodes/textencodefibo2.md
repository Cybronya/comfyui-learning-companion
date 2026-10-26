# TextEncodeFibo2

## 节点类型

`TextEncodeFibo2`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `clip:CLIP`（9 次）
- `images.image_1:IMAGE`（9 次）
- `images.image_2:IMAGE`（9 次）
- `images.image_3:IMAGE`（9 次）
- `vae:VAE`（9 次）
- `prompt:STRING`（9 次）
- `negative_prompt:STRING`（9 次）
- `width:INT`（9 次）
- `height:INT`（9 次）
- `batch_size:INT`（9 次）

## 输出

- `positive:CONDITIONING`（9 次）
- `negative:CONDITIONING`（9 次）
- `latent:LATENT`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Premium editorial perfume campaign photograph inside a modern glasshouse just after rain. Exactly one adult woman with`（3 次）
- `["A realistic product photograph of exactly six pieces of fruit arranged in one straight horizontal row on a dark wooden`（2 次）
- `["In <image_1>, find ONLY the adult woman slightly left of center in the foreground who is wearing the distinctive musta`（1 次）
- `["{\"short_description\":\"Realistic tabletop photograph of five red apples and one green pear arranged together in one `（1 次）
- `["{\"short_description\":\"Exactly six fruits in one straight horizontal row: red apple, green pear, red apple, red appl`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
