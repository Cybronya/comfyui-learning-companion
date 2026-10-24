---
name: text_to_image_sampler_clip_unet_105
type: Text To Image
frequency: 6
level: moderate
coverage: 0.873333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/-全能图片V1手办模型盲盒生成_1963979415220834306.json, 图片生成/图生图/87time #25 Kontext_1955478993660100609.json, 图片生成/图生图/Baihao-Kontext服装花型提取加强版_1948766748095983618.json, 图片生成/图生图/Flux Kontext Dev双图潜空间组合_1940046702055395329.json, 图片生成/图生图/Flux-Kontext-dev多图图像融合版_1938446557656342529.json, 图片生成/图生图/服装面料材质印花提取_1979006256419606530.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/-全能图片V1手办模型盲盒生成_1963979415220834306.json、图片生成/图生图/87time #25 Kontext_1955478993660100609.json、图片生成/图生图/Baihao-Kontext服装花型提取加强版_1948766748095983618.json、图片生成/图生图/Flux Kontext Dev双图潜空间组合_1940046702055395329.json、图片生成/图生图/Flux-Kontext-dev多图图像融合版_1938446557656342529.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 5/6 个有
- `ImageStitch` —— 4/6 个有
- `FluxKontextImageScale` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `FluxResolutionNode` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `MagCache` —— 1/6 个有
- `RMBG` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 864 | 512 - 1248 | 6 | 68% |
| 高度 | 928 | 512 - 1536 | 6 | 59% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 864，观测区间 512 - 1248，6 个样本
- 高度 中位数 928，观测区间 512 - 1536，6 个样本
