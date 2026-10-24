---
name: text_to_image_controlnet_sampler_clip_8
type: Text To Image
frequency: 6
level: strong
coverage: 0.967
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/根据提示词合并两张图片（简单工作流）_2068647438591807490.json, 图片生成/文生图/ComfyUI官方介绍中的控制生图工作流_1935504433507651585.json, 图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json, 图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json, 图片生成/文生图/ComfyUi官方介绍中的姿态控制工作流_1935513540252073985.json, 图片生成/文生图/姿态控制人像生成_1996127763935477761.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/根据提示词合并两张图片（简单工作流）_2068647438591807490.json、图片生成/文生图/ComfyUI官方介绍中的控制生图工作流_1935504433507651585.json、图片生成/文生图/ComfyUI官方示例10：混合控制ControlNet工作流 _ ComfyUI从入门到精通_1932448769386672129.json、图片生成/文生图/ComfyUI官方示例8：姿势控制ControlNet工作流 _ ComfyUI从入门到精通_1932443425478471681.json、图片生成/文生图/ComfyUi官方介绍中的姿态控制工作流_1935513540252073985.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ControlNetApplyAdvanced` —— 5/6 个有
- `CLIPSetLastLayer` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `CLIPTextEncodeSDXL` —— 1/6 个有
- `ControlNetApply` —— 1/6 个有
- `LatentUpscale` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 7 | 6 - 8 | 6 | 90% |
| 采样算法 | dpmpp_2m | - | 6 | 50% |
| 调度器 | karras | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| ControlNet 权重 | 1 | 0.7 - 1 | 6 | 88% |
| 宽度 | 1024 | 768 - 1024 | 6 | 90% |
| 高度 | 1024 | 768 - 1024 | 6 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 8，6 个样本，取值集中（一致性 90%）
- 采样算法 最常用 dpmpp_2m，6 个样本，一致性 50%
- 调度器 最常用 karras，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.7 - 1，6 个样本，取值集中（一致性 88%）
- 宽度 中位数 1024，观测区间 768 - 1024，6 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 768 - 1024，6 个样本，取值集中（一致性 90%）
