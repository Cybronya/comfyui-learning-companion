# PiDTextPrompt

## 节点类型

`PiDTextPrompt`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 15 个 workflow 中。

## 输入

- `prompt:STRING`（15 次）

## 输出

- `text:STRING`（15 次）
- `caption:STRING`（15 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["（电影级面光：1.6），（光线追踪：1.5），（冷白皮漫感质感的光滑皮肤：1.7），（人物有最好的骨相：1.2），（网感脸：1.6），身材完美，莫兰迪配色，高颜值网红，INS风，19岁女生尖下巴，三庭五眼比例均衡，细腻陶瓷水嫩肌肤，偏冷`（7 次）
- `["ASTRAL FORGE style cinematic fantasy realism, a noble star cartographer standing inside a vast brass observatory, velv`（1 次）
- `["High-end commercial product photograph for a luxury skincare bottle named \"AURORA N7\". Frosted glass pump bottle on `（1 次）
- `["A clean Art Nouveau poster for a fictional botanical tea house. The main readable title says \"MOON GARDEN\" in elegan`（1 次）
- `["dark_fantasy_illustration, retro dark fantasy book cover art, a lone silver-haired ranger crossing a ruined bridge ove`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
