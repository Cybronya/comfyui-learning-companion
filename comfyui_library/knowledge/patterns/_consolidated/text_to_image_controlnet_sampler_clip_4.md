---
name: text_to_image_controlnet_sampler_clip_4
type: Text To Image
frequency: 9
level: strong
coverage: 0.962222
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/根据提示词合并两张图片（简单工作流）_2068647438591807490.json, 图片生成/文生图/ComfyUI官方介绍中的控制生图工作流_1935504433507651585.json, 图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json, 图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json, 图片生成/文生图/ComfyUi官方介绍中的姿态控制工作流_1935513540252073985.json, 图片生成/文生图/姿态控制人像生成_1996127763935477761.json, 平台全量/ComfyUI官方示例7：边缘检测ControlNet工作流 _ ComfyUI从入门到精通_1932403183488540674.json, 平台全量/Lineart动漫上色_1978415374947520513.json, 平台全量/softedge软边缘_1978395783546474498.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/根据提示词合并两张图片（简单工作流）_2068647438591807490.json、图片生成/文生图/ComfyUI官方介绍中的控制生图工作流_1935504433507651585.json、图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json、图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json、图片生成/文生图/ComfyUi官方介绍中的姿态控制工作流_1935513540252073985.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 8/9 个有
- `PreviewImage` —— 5/9 个有
- `CLIPSetLastLayer` —— 3/9 个有
- `GetImageSize+` —— 2/9 个有
- `CLIPTextEncodeSDXL` —— 1/9 个有
- `ControlNetApply` —— 1/9 个有
- `HEDPreprocessor` —— 1/9 个有
- `LatentUpscale` —— 1/9 个有
- `LineArtPreprocessor` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 9 | 90% |
| Prompt 约束强度(CFG) | 6.5 | 6 - 8 | 9 | 91% |
| 采样算法 | dpmpp_2m | - | 9 | 33% |
| 调度器 | karras | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 1 | 0.7 - 1 | 9 | 90% |
| 宽度 | 1024 | 768 - 1024 | 9 | 87% |
| 高度 | 1024 | 768 - 1024 | 9 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，9 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 6 - 8，9 个样本，取值集中（一致性 91%）
- 采样算法 最常用 dpmpp_2m，9 个样本，一致性 33%
- 调度器 最常用 karras，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.7 - 1，9 个样本，取值集中（一致性 90%）
- 宽度 中位数 1024，观测区间 768 - 1024，9 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 768 - 1024，9 个样本，取值集中（一致性 92%）
