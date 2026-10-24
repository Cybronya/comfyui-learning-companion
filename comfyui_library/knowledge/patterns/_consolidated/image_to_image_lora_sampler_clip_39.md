---
name: image_to_image_lora_sampler_clip_39
type: Image To Image
frequency: 7
level: strong
coverage: 0.979571
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext3D场景融图工作流_1946053058235166721.json, 图片生成/图生图/KontextDev转绘JOJO动画风格_1942013323561037825.json, 图片生成/图生图/KontextDev转绘扁平化风_1942049063250640898.json, 图片生成/图生图/KontextDev转绘美漫风格_1942043248150134785.json, 图片生成/图生图/KontextNunchakuDev3D游戏动画_1942411012631105537.json, 图片生成/图生图/KontextNunchakuDevInpaintingRedux换装_1945000724100210689.json, 图片生成/图生图/双融图合并工作流_1983413939042197505.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Kontext3D场景融图工作流_1946053058235166721.json、图片生成/图生图/KontextDev转绘JOJO动画风格_1942013323561037825.json、图片生成/图生图/KontextDev转绘扁平化风_1942049063250640898.json、图片生成/图生图/KontextDev转绘美漫风格_1942043248150134785.json、图片生成/图生图/KontextNunchakuDev3D游戏动画_1942411012631105537.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 5/7 个有
- `UNETLoader` —— 5/7 个有
- `RH_Translator` —— 4/7 个有
- `easy imageRemBg` —— 3/7 个有
- `FastCanvas` —— 2/7 个有
- `FastCanvasTool` —— 2/7 个有
- `ModelSamplingFlux` —— 2/7 个有
- `NunchakuFluxDiTLoader` —— 2/7 个有
- `TeaCache` —— 2/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `ImageStitch` —— 1/7 个有
- `Kontext Inpainting Conditioning` —— 1/7 个有
- `ReduxAdvanced` —— 1/7 个有
- `SDXLPromptStyler` —— 1/7 个有
- `StyleModelLoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
