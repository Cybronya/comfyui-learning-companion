---
name: unknown_workflow_upscale_lora_sampler_130
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9165
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, ImageUpscaleWithModel, KSamplerSelect, LoraLoader, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Nunchaku_Flux高质量文生图+3lora+放大重绘_1932243038507364353.json, 平台全量/石矶娘娘的直播间_1897192342321844225.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_130

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Nunchaku_Flux高质量文生图+3lora+放大重绘_1932243038507364353.json、平台全量/石矶娘娘的直播间_1897192342321844225.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoraLoader`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxResolutionNode` —— 1/2 个有
- `Image Resize` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy imageSize` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | - | 2 | 89% |
| 高度 | 1000 | - | 2 | 72% |
| LoRA 模型强度 | 0.65 | - | 2 | 92% |
| LoRA 文本强度 | 0.8 | - | 2 | 75% |
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 30 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 高度 中位数 1000，样本不足，未给区间，2 个样本
- LoRA 模型强度 中位数 0.65，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
