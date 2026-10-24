---
name: image_to_image_sampler_unet_vae_34
type: Image To Image
frequency: 7
level: strong
coverage: 0.825143
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext  保持风格一键Teache加速扩图_1961480141107085314.json, 图片生成/图生图/Flux Kontext本地图片编辑王者_1938601592583344129.json, 图片生成/图生图/Flux+Kontext老照片修复_1949376700114731009.json, 图片生成/图生图/Flux-Kontext-Dev单图编辑极速工作流_1938581341325680641.json, 图片生成/图生图/KonText一句话P图！提示词改图=开源版=艾橘溪_1928485579321909249.json, 图片生成/图生图/KonText一句话改图，技术有限，创意无限！_1941126778633273346.json, 图片生成/图生图/flux_kontext图像编辑_万物玻璃_1961470553272029186.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux Kontext  保持风格一键Teache加速扩图_1961480141107085314.json、图片生成/图生图/Flux Kontext本地图片编辑王者_1938601592583344129.json、图片生成/图生图/Flux+Kontext老照片修复_1949376700114731009.json、图片生成/图生图/Flux-Kontext-Dev单图编辑极速工作流_1938581341325680641.json、图片生成/图生图/KonText一句话P图！提示词改图=开源版=艾橘溪_1928485579321909249.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
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
- `PreviewImage` —— 6/7 个有
- `CLIPTextEncode` —— 5/7 个有
- `FluxKontextImageScale` —— 5/7 个有
- `ImageStitch` —— 4/7 个有
- `RH_Translator` —— 3/7 个有
- `TeaCache` —— 3/7 个有
- `CLIPTextEncodeFlux` —— 2/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `ShowText|pysssss` —— 2/7 个有
- `Bjornulf_ShowStringText` —— 1/7 个有
- `ImagePadKJ` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `RMBG` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
