---
name: unknown_workflow_sampler_clip_unet_184
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.968143
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, Flux2Scheduler, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换脸Flux2Klein全能编辑20版人物一致自然真实多图编辑加速版_2058558786536828930.json, 图片生成/图生图/换脸Flux2Klein全能编辑20版人物一致自然真实多图编辑加速版_2075718981842980866.json, 图片生成/图生图/换脸Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012770534232170497.json, 图片生成/图生图/换脸Flux2Klein多图编辑4B加速版_2057827199104929793.json, 图片生成/图生图/换脸_2052716812382547970.json, 图片生成/图生图/换脸换人换衣服 写实换装 人物一致 Flux2-Klein9b 保留服饰细节 多图编辑 多图编辑_2100011899302797314.json, 图片生成/图生图/换脸换人换衣服_写实换装_人物一致_Flux2-Klein9b_保留服饰细节_多图编辑_多图编辑_2101216470276595714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_184

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/换脸Flux2Klein全能编辑20版人物一致自然真实多图编辑加速版_2058558786536828930.json、图片生成/图生图/换脸Flux2Klein全能编辑20版人物一致自然真实多图编辑加速版_2075718981842980866.json、图片生成/图生图/换脸Flux2Klein多图编辑4B加速版Flux2Klein多图编辑4B加速版_2012770534232170497.json、图片生成/图生图/换脸Flux2Klein多图编辑4B加速版_2057827199104929793.json、图片生成/图生图/换脸_2052716812382547970.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 6/7 个有
- `JWFloat` —— 5/7 个有
- `PreviewImage` —— 4/7 个有
- `ImageScaleBy` —— 2/7 个有
- `Int` —— 2/7 个有
- `KSamplerAdvanced` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ModelSamplingAuraFlow` —— 2/7 个有
- `RH_Captioner` —— 2/7 个有
- `RunningHub Deepcleaner` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `EmptyImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 9 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta57 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta57，2 个样本，一致性 100%
