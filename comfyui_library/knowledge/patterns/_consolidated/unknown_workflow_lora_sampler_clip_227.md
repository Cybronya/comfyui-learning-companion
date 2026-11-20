---
name: unknown_workflow_lora_sampler_clip_227
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.828
common_nodes: [ApplyPulidFlux, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人物一致性--多图多美女融合--小红书风格_1878634199812055041.json, 平台全量/4pics_1852641002086408193.json, 平台全量/PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_227

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物一致性--多图多美女融合--小红书风格_1878634199812055041.json、平台全量/4pics_1852641002086408193.json、平台全量/PuLID-Flux_ Unlock Your Creativity by 金运_1841525689001672706.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCrop+` —— 2/3 个有
- `JoinStringMulti` —— 2/3 个有
- `LayerUtility: JoyCaption2` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `Efficient Loader` —— 1/3 个有
- `KSampler (Efficient)` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `XY Input: LoRA Plot` —— 1/3 个有
- `XY Plot` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
