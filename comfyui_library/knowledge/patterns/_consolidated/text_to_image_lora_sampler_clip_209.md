---
name: text_to_image_lora_sampler_clip_209
type: Text To Image
frequency: 9
level: strong
coverage: 0.874444
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3图片换头 图生视频人物替换处理生成工具_2100269102773395458.json, 视频生成/图生视频/H3图片换头生视频 图生视频创作处理工具_2100267469515608066.json, 视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json, 视频生成/图生视频/MiniMax H3图生视频首尾帧控制｜原生音频自带，两张图变一段电影感短片_2100451183075880961.json, 视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json, 视频生成/图生视频/MiniMaxH3参考生视频量化加速版｜文本图像音频视频全模态，图生视频更快出活_2100449477902553090.json, 视频生成/图生视频/声音）4步lora视频MinimaxH3-多参生视频（图片_2087336403087745025.json, 视频生成/文生视频/H3参考生视频量化加速版文本图像音频视频多模态_2100678580580732929.json, 视频生成/文生视频/海螺MiniMax H3开源版Turbo全模式视频整合流处理工具_2101755741546835970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_209

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/H3图片换头 图生视频人物替换处理生成工具_2100269102773395458.json、视频生成/图生视频/H3图片换头生视频 图生视频创作处理工具_2100267469515608066.json、视频生成/图生视频/MiniMax H3参考生视频加速版｜加速LoRA图生视频生成_2097403914214789122.json、视频生成/图生视频/MiniMax H3图生视频首尾帧控制｜原生音频自带，两张图变一段电影感短片_2100451183075880961.json、视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 8/9 个有
- `MiniMaxH3ReferenceToVideo` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `PrimitiveFloat` —— 7/9 个有
- `ResolutionSelector` —— 7/9 个有
- `LoadAudio` —— 6/9 个有
- `SaveImage` —— 6/9 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/9 个有
- `PreviewImage` —— 5/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `EmptyImage` —— 3/9 个有
- `Int` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `CR Color Panel` —— 2/9 个有
- `GetImageSize` —— 2/9 个有
- `ImageCompositeMasked` —— 2/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/9 个有
- `MiniMaxH3ImageToVideo` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `RH_LLMAPI_Pro_Node` —— 2/9 个有
- `Seed (rgthree)` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `GetVideoComponents` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `LoadVideo` —— 1/9 个有
- `MuyeTextEditOutput` —— 1/9 个有
- `PlaySound|pysssss` —— 1/9 个有
- `easy saveVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
