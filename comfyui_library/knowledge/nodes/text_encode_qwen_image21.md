# TextEncodeQwenImage21

## 节点类型

`TextEncodeQwenImage21`

## 分类

Text Conditioning（Qwen Image 2.1 专属）

## 作用

Qwen Image 2.1 的专用文本编码节点：把正向/负向提示词编码成
conditioning，内置 2.1 模型族的提示词处理逻辑，替代通用的
`CLIPTextEncode`。

## 参数（统计自 404 个真实 workflow，178 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| prompt / positive | 正向提示词 | 多数留空（配合图生图用指令式提示词） |
| negative | 负向提示词 | 高频固定串：blurry, lowres, bad anatomy, deformed, extra limbs... |
| width/height 类数值 | 目标分辨率 | 1024 居多，部分 0（跟随输入图） |

## 常见问题与风险

- 必须接 `CLIPLoader`（type=qwen_image）输出的 CLIP，
  接其他编码器的 CLIP 不会有报错但提示词失效。
- Qwen Image 对长文本、文字排版指令敏感，提示词可以直接写
  「图上要显示的字」，这是它相对 SD 系的主要优势。

## 可信度

Generated（2026-10-06，参数分布实测；输入输出连线为通行语义）TODO(待验证)
