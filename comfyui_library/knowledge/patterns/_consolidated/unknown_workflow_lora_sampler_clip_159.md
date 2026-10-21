---
name: unknown_workflow_lora_sampler_clip_159
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8775
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1951667086886121474.json, 图片生成/文生图/1954712659226705921.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1951667086886121474.json、图片生成/文生图/1954712659226705921.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `NunchakuTextEncoderLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ChinesePrompt_Mix` —— 1/2 个有
- `ClownOptions_DetailBoost_Beta` —— 1/2 个有
- `ClownOptions_SwapSampler_Beta` —— 1/2 个有
- `ClownsharKSampler_Beta` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Int` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SharkOptions_Beta` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | bong_tangent | - | 1 | 100% |
| Prompt 约束强度(CFG) | 10 | - | 1 | 100% |
| 采样算法 | -1 | - | 1 | 100% |
| 调度器 | -0.67 | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：重绘幅度 观测到 1，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
