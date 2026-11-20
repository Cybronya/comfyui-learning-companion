---
name: unknown_workflow_sampler_clip_unet_303
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.91925
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【最新】Flux 局部重绘技术_1915011533284306945.json, 图片生成/文生图/FLUX批量生成小红书涨粉美女_1884421093896372225.json, 图片生成/文生图/flux文生图 小白友好_1913620524503891969.json, 图片生成/文生图/【FLUX一键批量生成】【小红书涨粉美女 】_1909203282877624322.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_303

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【最新】Flux 局部重绘技术_1915011533284306945.json、图片生成/文生图/FLUX批量生成小红书涨粉美女_1884421093896372225.json、图片生成/文生图/flux文生图 小白友好_1913620524503891969.json、图片生成/文生图/【FLUX一键批量生成】【小红书涨粉美女 】_1909203282877624322.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/4 个有
- `LoraLoader|pysssss` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `ImpactGaussianBlurMask` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `LoadAndResizeImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1.72 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1.72，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
