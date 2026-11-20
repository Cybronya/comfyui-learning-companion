---
name: image_to_image_sampler_unet_vae_42
type: Image To Image
frequency: 7
level: strong
coverage: 0.938
common_nodes: [DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/Kontext线稿生成_2042468381122629634.json, 平台全量/人像逆光摄影_1964558494089232385.json, 平台全量/全能视频S制作真人视频素描图工作流素描图直出工作流_1978131449578676225.json, 平台全量/全能视频S真人前置-素描Kontext-t8_1974755666818633729.json, 平台全量/全能视频S真人前置素描（根叔）_1977767580381446145.json, 平台全量/冬季雪景氛围_1946955450778836994.json, 平台全量/四季变化  四季更替   全能图片V1 2 pro 季节变换 影楼摄影 婚纱摄影 春夏秋冬_2002643524229165058.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Kontext线稿生成_2042468381122629634.json、平台全量/人像逆光摄影_1964558494089232385.json、平台全量/全能视频S制作真人视频素描图工作流素描图直出工作流_1978131449578676225.json、平台全量/全能视频S真人前置-素描Kontext-t8_1974755666818633729.json、平台全量/全能视频S真人前置素描（根叔）_1977767580381446145.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
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
- `CLIPTextEncode` —— 6/7 个有
- `ConditioningZeroOut` —— 6/7 个有
- `FluxKontextImageScale` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `ConstrainImage|pysssss` —— 2/7 个有
- `Bookmark (rgthree)` —— 1/7 个有
- `CR Simple Image Compare` —— 1/7 个有
- `Fast Bypasser (rgthree)` —— 1/7 个有
- `LoadDiffusionModelShared //Inspire` —— 1/7 个有
- `LoadTextEncoderShared //Inspire` —— 1/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `RH_Nano_Banana2_Image2Image` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
