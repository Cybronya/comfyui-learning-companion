---
name: text_to_image_lora_sampler_clip_22
type: Text To Image
frequency: 24
level: strong
coverage: 0.891083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json, 视频生成/图生视频/H3文生视频加速版｜快速直出高质量视频生成_2094509372390076418.json, 视频生成/图生视频/H3稳定加速版整合打斗和脸部修复Lora_2100265879845040129.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2088772291898466305.json, 视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2090466751896178689.json, 视频生成/图生视频/H3音频驱动数字人单人版｜口播视频高质量生成_2094900079206424577.json, 视频生成/图生视频/MiniMax H3 I2V加速多参考视频生成工作流，图生视频高效创作工具_2106861353209253890.json, 视频生成/图生视频/MiniMax H3 I2V加速首尾帧工作流，图生视频高效创作工具_2106838741942886401.json, 视频生成/图生视频/MiniMax H3全能参考工作流 多模态输入视频生成_2105367688095821826.json, 视频生成/图生视频/MiniMax H3全能参考工作流｜图生视频万能底座_2105278066246373377.json, 视频生成/图生视频/MiniMax H3单人音频驱动数字人 最高15秒视频生成_2099176616411881474.json, 视频生成/图生视频/MiniMax-H3音频数字人来了｜单人出镜最高15秒，口播带货省事_2099401548009918466.json, 视频生成/图生视频/单人数字人直播｜MiniMax H3图生视频驱动口播_2089027921309691906.json, 视频生成/图生视频/单人版数字人直播｜MiniMax H3图生视频口播生成_2088700833398607873.json, 视频生成/图生视频/单人版音频驱动数字人｜H3图生视频对口型生成_2095092471347900417.json, 视频生成/图生视频/单人音频驱动数字人（最高15秒）MiniMax-H3_2087437541388673025.json, 视频生成/图生视频/开源稳定加速版全能参考｜MiniMax H3支持自定义音频图生视频_2091285576120102913.json, 视频生成/图生视频/稳定加速5参考图版｜MiniMax H3全能参考自定义音频_2091200766919925762.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3五参考图音频自定义_2090900087277973505.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3开源支持自定义音频_2091271985484623874.json, 视频生成/图生视频/稳定加速版全能参考｜MiniMax H3支持自定义音频_2092396498217689090.json, 视频生成/图生视频/稳定加速版｜MiniMax H3 全能参考4步加速_2089295207438307330.json, 音频生成/音频生成/声音克隆音频生成｜H3语音克隆工作流_2088159396017827842.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json、视频生成/图生视频/H3文生视频加速版｜快速直出高质量视频生成_2094509372390076418.json、视频生成/图生视频/H3稳定加速版整合打斗和脸部修复Lora_2100265879845040129.json、视频生成/图生视频/H3角色替换图生视频｜视频人物一键换脸替换生成_2088772291898466305.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `KSamplerSelect` —— 23/24 个有
- `孤海注释` —— 23/24 个有
- `LoadImage` —— 22/24 个有
- `PrimitiveFloat` —— 22/24 个有
- `ResolutionSelector` —— 22/24 个有
- `PrimitiveStringMultiline` —— 21/24 个有
- `ComfyMathExpression` —— 19/24 个有
- `LoadAudio` —— 18/24 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 18/24 个有
- `VHS_VideoCombine` —— 17/24 个有
- `LoraLoaderBypassModelOnly` —— 15/24 个有
- `VAEDecodeAudio` —— 15/24 个有
- `CreateVideo` —— 13/24 个有
- `SaveImage` —— 13/24 个有
- `SaveVideo` —— 13/24 个有
- `MiniMaxH3ReferenceToVideo` —— 12/24 个有
- `PathchSageAttentionKJ` —— 10/24 个有
- `AudioCrop` —— 8/24 个有
- `MiniMaxH3AudioConditioningT8` —— 7/24 个有
- `MiniMaxH3DualClockSamplerT8` —— 7/24 个有
- `SoundFlow_GetLength` —— 7/24 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 7/24 个有
- `FlashVSRNode` —— 6/24 个有
- `Sleep` —— 6/24 个有
- `MathExpression|pysssss` —— 4/24 个有
- `VHS_LoadVideo` —— 4/24 个有
- `CR Prompt Text` —— 3/24 个有
- `LayerUtility: PurgeVRAM V2` —— 3/24 个有
- `MiniMaxH3ImageToVideo` —— 3/24 个有
- `PreviewAudio` —— 3/24 个有
- `Fast Groups Bypasser (rgthree)` —— 2/24 个有
- `SFH3MultimodalDirector` —— 2/24 个有
- `Audio Duration (mtb)` —— 1/24 个有
- `Label (rgthree)` —— 1/24 个有
- `PainterVRAM` —— 1/24 个有
- `ProcessString` —— 1/24 个有
- `SaveAudioAdvanced` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 24 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 24 | 100% |
| 采样算法 | er_sde | - | 24 | 100% |
| 调度器 | beta | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 80 | 80 - 80 | 24 | 100% |
| 高度 | 80 | 80 - 80 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，24 个样本，一致性 100%
- 调度器 最常用 beta，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，24 个样本，取值集中（一致性 100%）
- 高发问题（25/24 个样本）：Steps较低可能导致细节不足
