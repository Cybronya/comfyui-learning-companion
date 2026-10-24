---
name: unknown_workflow_sampler_clip_vae_40
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.928333
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/Flux.1 Krea 文生图工作流（高清+去除AI感）_1970368325295480834.json, 图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json, 图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json, 图片生成/文生图/Flux文生图工作流原版FP16_1965805471892443137.json, 图片生成/文生图/Flux稳定生成文字_1819769505672531969.json, 图片生成/文生图/Flux稳定生成文字_1824318987025952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Flux.1 Krea 文生图工作流（高清+去除AI感）_1970368325295480834.json、图片生成/文生图/Flux.1 Krea文生图_1951132199200432130.json、图片生成/文生图/Flux.1文生图工作流（高清+去除AI感）_1954823552040091649.json、图片生成/文生图/Flux文生图工作流原版FP16_1965805471892443137.json、图片生成/文生图/Flux稳定生成文字_1819769505672531969.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `VAELoader` —— 5/6 个有
- `PreviewImage` —— 3/6 个有
- `CFGZeroStar` —— 2/6 个有
- `CLIPTextEncodeFlux` —— 2/6 个有
- `CR SDXL Aspect Ratio` —— 2/6 个有
- `KSamplerAdvanced` —— 2/6 个有
- `Lora Loader Stack (rgthree)` —— 2/6 个有
- `StringConstantMultiline` —— 2/6 个有
- `CheckpointLoaderSimple` —— 1/6 个有
- `FluxGuidance` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 6 | 97% |
| 高度 | 1280 | 1024 - 1920 | 6 | 71% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 31 | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，6 个样本，取值集中（一致性 97%）
- 高度 中位数 1280，观测区间 1024 - 1920，6 个样本
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 31，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 31，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
