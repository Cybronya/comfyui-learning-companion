---
name: text_to_image_lora_sampler_clip_21
type: Text To Image
frequency: 27
level: strong
coverage: 0.813667
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/H3开源数字人自动版工作流，唱歌说唱口播带货虚拟主播全能_2115007525472002050.json, 图片生成/图生图/Minimax h3高一致性工作流｜多镜头音频参考视频生成_2097838671696318466.json, 数字人/数字人/MiniMax-H3开源数字人全自动｜电商产品讲解虚拟主播_2111812476277972994.json, 数字人/数字人/MiniMax-H3开源数字人自动版，唱歌说唱口播电商讲解_2111912691190288386.json, 数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播带货_2111783890280083457.json, 数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解_2090069695356563458.json, 数字人/数字人/MiniMax-H3开源数字人，唱歌口播虚拟主播自动版_2111919197029748738.json, 视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜_2091171813098344450.json, 视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜图生视频_2091249300000034818.json, 视频生成/图生视频/15秒卡点混剪｜MinimaxH3像素幻想Lab转场特效_2090885714388013057.json, 视频生成/图生视频/H3多图数字人最新优化版 多图参考数字人视频生成_2099199642356510721.json, 视频生成/图生视频/MiniMax H3多图参考数字人唱歌精准对话 数字人口播方案_2109353184165715970.json, 视频生成/图生视频/MiniMax H3开源数字人唱歌说唱口播虚拟主播电商产品讲解自动版工作流_2107966601273372673.json, 视频生成/图生视频/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解角色设计_2090077928905330689.json, 视频生成/图生视频/MiniMax-H3开源数字人｜唱歌口播虚拟主播全自动版_2107672106023608321.json, 视频生成/图生视频/MiniMax-H3开源数字人｜唱歌说唱口播虚拟主播电商讲解_2095217698312642562.json, 视频生成/图生视频/MiniMaxH3多图数字人优化新版｜多图驱动更稳，口播视频更自然_2099508624107335682.json, 视频生成/图生视频/MiniMaxH3多图数字人最新优化版｜图生视频驱动口播人物更自然_2101848347656146946.json, 视频生成/图生视频/口播说唱唱歌电商讲解｜MiniMax H3自动数字人_2091192351791341570.json, 视频生成/图生视频/开源数字人自动版｜MiniMax-H3唱歌说唱口播讲解_2093766167809843202.json, 视频生成/图生视频/开源数字人｜MiniMax H3唱歌说唱口播全能，虚拟主播自动生成_2099920276535463937.json, 视频生成/图生视频/数字人唱歌说唱口播｜MiniMax-H3开源虚拟主播电商讲解自动版_2095554696181272577.json, 视频生成/图生视频/数字人唱歌说唱口播｜MiniMax-H3开源虚拟主播讲解_2093436709731127298.json, 视频生成/图生视频/数字人自动版｜MiniMax-H3唱歌说唱口播虚拟主播产品讲解_2089792313785675777.json, 视频生成/图生视频/虚拟主播电商产品讲解｜MiniMax-H3开源数字人唱歌说唱自动版_2095556325643210753.json, 视频生成/文生视频/MiniMaxH3多图数字人生成｜文生视频多图驱动_2094504932195000321.json, 视频生成/文生视频/多图数字人生成｜MiniMaxH3文生图生视频工作流_2094729429032464385.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/H3开源数字人自动版工作流，唱歌说唱口播带货虚拟主播全能_2115007525472002050.json、图片生成/图生图/Minimax h3高一致性工作流｜多镜头音频参考视频生成_2097838671696318466.json、数字人/数字人/MiniMax-H3开源数字人全自动｜电商产品讲解虚拟主播_2111812476277972994.json、数字人/数字人/MiniMax-H3开源数字人自动版，唱歌说唱口播电商讲解_2111912691190288386.json、数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播带货_2111783890280083457.json…）

- **类型**：Text To Image
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 26/27 个有
- `VHS_VideoCombine` —— 26/27 个有
- `llama_cpp_instruct_adv` —— 26/27 个有
- `llama_cpp_model_loader` —— 26/27 个有
- `llama_cpp_parameters` —— 26/27 个有
- `LoadAudio` —— 24/27 个有
- `Audio Duration (mtb)` —— 23/27 个有
- `AudioCrop` —— 23/27 个有
- `AudioSeparation` —— 23/27 个有
- `MathExpression|pysssss` —— 23/27 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 23/27 个有
- `ComfyMathExpression` —— 21/27 个有
- `PrimitiveFloat` —— 21/27 个有
- `GetNode` —— 18/27 个有
- `SetNode` —— 18/27 个有
- `SaveText` —— 17/27 个有
- `SaveImage` —— 7/27 个有
- `Fast Groups Bypasser (rgthree)` —— 6/27 个有
- `easy float` —— 6/27 个有
- `VAEDecodeAudio` —— 4/27 个有
- `H3SigmaRefiner` —— 3/27 个有
- `MiniMaxH3AddGuide` —— 1/27 个有
- `MuyeTextEditOutput` —— 1/27 个有
- `PreviewImage` —— 1/27 个有
- `SaveVideo` —— 1/27 个有
- `VideoCombineV2` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 27 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 27 | 100% |
| 采样算法 | er_sde | - | 27 | 100% |
| 调度器 | beta | - | 27 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 27 | 100% |
| 宽度 | 80 | 80 - 80 | 27 | 100% |
| 高度 | 80 | 80 - 80 | 27 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/27 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，27 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，27 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，27 个样本，一致性 100%
- 调度器 最常用 beta，27 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，27 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，27 个样本，取值集中（一致性 100%）
- 高发问题（28/27 个样本）：Steps较低可能导致细节不足
