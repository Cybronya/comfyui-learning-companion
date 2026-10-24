# Comfly_Flux_Kontext_Edit

## 节点类型

`Comfly_Flux_Kontext_Edit`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `prompt:STRING`（4 次）
- `aspect_ratio:COMBO`（4 次）
- `model:COMBO`（3 次）
- `apikey:STRING`（3 次）
- `num_of_images:INT`（3 次）
- `seed:INT`（3 次）

## 输出

- `image:IMAGE`（4 次）
- `image_url:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "flux-kontext-pro", "", "1:1", 1, 1684484037, "randomize"]`（1 次）
- `["", "flux-kontext-pro", "", "1:1", 1, 810058173, "randomize"]`（1 次）
- `["", "flux-kontext-pro", "sk-pIsh8VOwG2Iz2Y0gCdBaE52483994a5bA2Ff43D51b7859E5", "4:3", 1, 59614995, "randomize"]`（1 次）
- `["", "flux-kontext-pro", "sk-Wz67SuGD3tzhcEJa27Ec09122bB848C6Ad10CfCd2b0c2cDe", "4:3", 1, 1711218432, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
