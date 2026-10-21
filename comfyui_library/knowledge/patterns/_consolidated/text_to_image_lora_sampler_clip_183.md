---
name: text_to_image_lora_sampler_clip_183
type: Text To Image
frequency: 7
level: strong
coverage: 0.886857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3双采口播工作流照片加文案自动配音数字人，图生视频数字人生成工具_2106080341093076994.json, 视频生成/图生视频/Kling 2.5首尾帧生视频｜两张图片变一段视频_2098769825513426945.json, 视频生成/图生视频/MiniMax H3上下文参考视频加图生视频融合运镜与角色工作流方案_2106081882151669762.json, 视频生成/图生视频/Seedance 2.0图生视频｜首尾帧双参可调，生成视频自带音频_2099906662617407490.json, 视频生成/图生视频/Seedance2.0 Global图生视频｜首尾帧4K视频生成工作流_2097815419359940610.json, 视频生成/图生视频/商品图一键变广告视频｜Seedance 1.5 Pro运镜带货短片_2106266731076476929.json, 视频生成/文生视频/H3 MAX智能运镜工作流AI看图自动运镜，文生视频图生视频静图动态化工具_2106083477107077121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_183

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/H3双采口播工作流照片加文案自动配音数字人，图生视频数字人生成工具_2106080341093076994.json、视频生成/图生视频/Kling 2.5首尾帧生视频｜两张图片变一段视频_2098769825513426945.json、视频生成/图生视频/MiniMax H3上下文参考视频加图生视频融合运镜与角色工作流方案_2106081882151669762.json、视频生成/图生视频/Seedance 2.0图生视频｜首尾帧双参可调，生成视频自带音频_2099906662617407490.json、视频生成/图生视频/Seedance2.0 Global图生视频｜首尾帧4K视频生成工作流_2097815419359940610.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `RHMiniMaxH3ModelLoader` —— 4/7 个有
- `RHMiniMaxH3TextEncoderLoader` —— 4/7 个有
- `RHMiniMaxH3VAELoader` —— 4/7 个有
- `SaveImage` —— 4/7 个有
- `RHMiniMaxH3RefGen` —— 3/7 个有
- `RHMiniMaxH3VideoGen` —— 2/7 个有
- `RH_BytedanceSeedance20GlobalImageToVideo` —— 2/7 个有
- `CR Prompt Text` —— 1/7 个有
- `OmniVoiceVoiceDesignTTS` —— 1/7 个有
- `RH_Kling25_I2V_FirstLastFrame` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
