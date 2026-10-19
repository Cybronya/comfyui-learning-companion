---
name: text_to_image_lora_sampler_clip_95
type: Text To Image
frequency: 9
level: strong
coverage: 0.76
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MiniMax H3快速动作一镜到底多图参考，文生图图生视频高效创作工具_2103959005801574402.json, 数字人/数字人/7度工作流改版1号｜数字人生成效果升级更自然_2106257948442972161.json, 数字人/数字人/7度工作流改版1数字人生成方案，数字人图像处理工具_2107527180271050754.json, 数字人/数字人/7度工作流改版1，数字人生成图像编辑多场景覆盖处理方案_2106524485028499458.json, 数字人/数字人/7度工作流改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107284908405248002.json, 数字人/数字人/人物场景替换工作流｜数字人一键换背景搬家不穿帮_2097578172031258626.json, 视频生成/图生视频/MiniMax H3参考生视频｜Sage加速高质量生成_2095214729747853313.json, 视频生成/文生视频/Minimax-H3VDN-R2V三模式生成｜RH在线流直跑_2097156284557643777.json, 视频生成/文生视频/Minimax-H3VDN-R2V视频生成｜RH在线流工作流制作_2097073901951086594.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/MiniMax H3快速动作一镜到底多图参考，文生图图生视频高效创作工具_2103959005801574402.json、数字人/数字人/7度工作流改版1号｜数字人生成效果升级更自然_2106257948442972161.json、数字人/数字人/7度工作流改版1数字人生成方案，数字人图像处理工具_2107527180271050754.json、数字人/数字人/7度工作流改版1，数字人生成图像编辑多场景覆盖处理方案_2106524485028499458.json、数字人/数字人/7度工作流改版1｜数字人视频生成利器，老牌工作流焕新升级再战_2107284908405248002.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：76%

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
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 8/9 个有
- `SetNode` —— 8/9 个有
- `MiniMaxH3SigmaShift` —— 7/9 个有
- `LoadAudio` —— 6/9 个有
- `CreateVideo` —— 5/9 个有
- `PathchSageAttentionKJ` —— 5/9 个有
- `SaveVideo` —— 5/9 个有
- `VHS_VideoCombine` —— 5/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `SaveImage` —— 4/9 个有
- `SolAttnPatch` —— 4/9 个有
- `ImageResizeKJv2` —— 3/9 个有
- `MiniMaxChunkFeedForward` —— 3/9 个有
- `MiniMaxH3VDNRuntimeAuditT8Advanced` —— 3/9 个有
- `MiniMaxLowVRAMAttention` —— 3/9 个有
- `ModelAttentionBackend` —— 3/9 个有
- `ModelPatchTorchSettings` —— 3/9 个有
- `StringConcatenate` —— 3/9 个有
- `VHS_LoadVideo` —— 2/9 个有
- `EasyCache` —— 1/9 个有
- `FlashVSRInitPipe` —— 1/9 个有
- `FlashVSRNodeAdv` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有

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
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
