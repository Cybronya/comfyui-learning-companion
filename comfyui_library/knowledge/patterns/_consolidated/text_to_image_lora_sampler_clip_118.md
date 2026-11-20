---
name: text_to_image_lora_sampler_clip_118
type: Text To Image
frequency: 13
level: strong
coverage: 0.886462
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/flux3_klien3文生图，人像写真平面设计出图_2111559376304693250.json, 图片生成/文生图/文生图工作流｜即梦图片4.6中文文字精准生成_2100836535871557633.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json, 视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json, 视频生成/图生视频/Minimax h3超级加速多图参考生视频 快速出片方案_2109357930280734721.json, 视频生成/图生视频/Seedance2.5图生视频工作流｜首尾帧4K长视频生成_2097830170391572482.json, 视频生成/图生视频/h3图生视频加速版快速出片高效生成工作流_2088357034935808002.json, 视频生成/图生视频/加速版图生视频｜H3高质量快速生成工作流_2095093795384811522.json, 视频生成/图生视频/加速版图生视频｜h3图片转视频工作流_2088324394362957826.json, 视频生成/图生视频/超级加速多图参考生视频｜Minimax_h3角色一致性角色表演工作流_2087208437443809281.json, 视频生成/文生视频/文生视频基础流｜Minimax_h3一键生成_2093223576789938178.json, 视频生成/文生视频/文生视频直出｜Minimax H3基础模型高质量生成_2093066954859966466.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/flux3_klien3文生图，人像写真平面设计出图_2111559376304693250.json、图片生成/文生图/文生图工作流｜即梦图片4.6中文文字精准生成_2100836535871557633.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json、视频生成/图生视频/I2V lora加速｜MiniMax H3首帧图生视频3分40秒_2091174539307872258.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 12/13 个有
- `KSamplerSelect` —— 12/13 个有
- `RandomNoise` —— 12/13 个有
- `SamplerCustomAdvanced` —— 12/13 个有
- `BasicScheduler` —— 11/13 个有
- `PrimitiveStringMultiline` —— 11/13 个有
- `VAEDecodeAudio` —— 11/13 个有
- `VHS_VideoCombine` —— 11/13 个有
- `ComfyMathExpression` —— 9/13 个有
- `LoadImage` —— 9/13 个有
- `PrimitiveFloat` —— 9/13 个有
- `SaveImage` —— 9/13 个有
- `ResolutionSelector` —— 8/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/13 个有
- `MiniMaxH3ImageToVideo` —— 6/13 个有
- `LoraLoaderBypassModelOnly` —— 5/13 个有
- `EasyCache` —— 4/13 个有
- `MiniMaxChunkFeedForward` —— 4/13 个有
- `MiniMaxLowVRAMAttention` —— 4/13 个有
- `PainterVRAM` —— 4/13 个有
- `PathchSageAttentionKJ` —— 4/13 个有
- `FlashVSRNode` —— 3/13 个有
- `MiniMaxH3ReferenceToVideo` —— 3/13 个有
- `Sleep` —— 3/13 个有
- `SolAttnPatch` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `SFH3MultimodalDirector` —— 2/13 个有
- `Int` —— 1/13 个有
- `ManualSigmas` —— 1/13 个有
- `ModelAttentionBackend` —— 1/13 个有
- `RH_BytedanceJimeng46TextToImage` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `ZNGB_ResizeImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
