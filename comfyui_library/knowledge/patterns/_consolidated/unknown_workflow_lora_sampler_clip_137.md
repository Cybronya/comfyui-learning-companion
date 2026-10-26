---
name: unknown_workflow_lora_sampler_clip_137
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86375
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 klein Ai模特换装工作流 试衣间_2053130177160458242.json, 图片生成/图生图/Flux2+Klein9b服装提取3d+移除褶皱_2020468089401384961.json, 图片生成/图生图/Flux2-Klein9b 万能提取服装_2025975423003271170.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换_1985311204883243009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_137

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 klein Ai模特换装工作流 试衣间_2053130177160458242.json、图片生成/图生图/Flux2+Klein9b服装提取3d+移除褶皱_2020468089401384961.json、图片生成/图生图/Flux2-Klein9b 万能提取服装_2025975423003271170.json、图片生成/图生图/Qwen-Edit-2509-多角度切换_1985311204883243009.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `QwenImageIntegratedKSampler` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy imageSize` —— 1/4 个有
- `easy loraStack` —— 1/4 个有
- `easy loraStackApply` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | 1472 | - | 1 | 100% |
| 调度器 | 1096 | - | 1 | 100% |
| 重绘幅度 | 1.30185e+14 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：重绘幅度 观测到 1.30185e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
