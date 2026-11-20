---
name: text_to_image_sampler_clip_unet_84
type: Text To Image
frequency: 8
level: strong
coverage: 0.90125
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/-全能图片V1手办模型盲盒生成_1963979415220834306.json, 图片生成/图生图/87time #25 Kontext_1955478993660100609.json, 图片生成/图生图/Baihao-Kontext服装花型提取加强版_1948766748095983618.json, 图片生成/图生图/Flux Kontext Dev双图潜空间组合_1940046702055395329.json, 图片生成/图生图/Flux-Kontext-dev多图图像融合版_1938446557656342529.json, 图片生成/图生图/服装面料材质印花提取_1979006256419606530.json, 平台全量/kontext一键生成四格漫画（保持漫画人物一致性）_1941669198471000066.json, 平台全量/同一ip生成4格漫画_1940753687704924161.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/-全能图片V1手办模型盲盒生成_1963979415220834306.json、图片生成/图生图/87time #25 Kontext_1955478993660100609.json、图片生成/图生图/Baihao-Kontext服装花型提取加强版_1948766748095983618.json、图片生成/图生图/Flux Kontext Dev双图潜空间组合_1940046702055395329.json、图片生成/图生图/Flux-Kontext-dev多图图像融合版_1938446557656342529.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `RH_Translator` —— 5/8 个有
- `FluxKontextImageScale` —— 3/8 个有
- `Text Multiline` —— 3/8 个有
- `ttN imageREMBG` —— 2/8 个有
- `FluxResolutionNode` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `MagCache` —— 1/8 个有
- `RMBG` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy imageSize` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 8 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 896 | 512 - 1248 | 8 | 72% |
| 高度 | 1088 | 512 - 1536 | 8 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，8 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 1248，8 个样本
- 高度 中位数 1088，观测区间 512 - 1536，8 个样本
