# ByteDance2TextToVideoNode

## 节点类型

`ByteDance2TextToVideoNode`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输出

- `VIDEO:VIDEO`（5 次）
- `draft_task_id:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Seedance 2.0 Mini", "[Style] Photorealistic futuristic space warfare, 8K, blockbuster fleet battle, cold silver hulls,`（1 次）
- `["Seedance 2.0", "[Style] Magical dreamspace couture fantasy, 8K ultra-clear, Photorealistic, High-fashion Editorial, fl`（1 次）
- `["Seedance 2.5 Draft", "**Cinematic rocket launch sequence, 5 seconds, IMAX blockbuster style, hard cuts between wide, m`（1 次）
- `["Seedance 2.5", "Classic western comedy, live-action, spaghetti western look, golden hour desert. Two bank robbers stum`（1 次）
- `["Seedance 2.5", "1990s American courtroom drama scene, live-action, film grain, wood-paneled courtroom. A hippo lawyer `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
