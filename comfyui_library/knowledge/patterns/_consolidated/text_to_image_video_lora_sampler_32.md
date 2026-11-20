---
name: text_to_image_video_lora_sampler_32
type: Text To Image
frequency: 20
level: strong
coverage: 0.77725
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3多图数字人最新优化版 多图参考数字人视频生成_2099199642356510721.json, 视频生成/图生视频/MiniMax H3多图参考数字人唱歌精准对话 数字人口播方案_2109353184165715970.json, 视频生成/图生视频/MiniMax H3开源数字人唱歌说唱口播虚拟主播电商产品讲解自动版工作流_2107966601273372673.json, 视频生成/图生视频/MiniMax H3极速多参视频制作，文生视频图生视频多模式高效出片_2114423427422576642.json, 视频生成/图生视频/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解角色设计_2090077928905330689.json, 视频生成/图生视频/MiniMax-H3开源数字人｜唱歌口播虚拟主播全自动版_2107672106023608321.json, 视频生成/图生视频/MiniMax-H3开源数字人｜唱歌说唱口播虚拟主播电商讲解_2095217698312642562.json, 视频生成/图生视频/MiniMaxH3-极速多参视频制作｜文生视频图生视频快到飞起_2114257352080846849.json, 视频生成/图生视频/MiniMaxH3多图数字人优化新版｜多图驱动更稳，口播视频更自然_2099508624107335682.json, 视频生成/图生视频/MiniMaxH3多图数字人最新优化版｜图生视频驱动口播人物更自然_2101848347656146946.json, 视频生成/图生视频/MiniMaxH3极速多参视频 加速Lora语义强化生成工具_2113350861492678657.json, 视频生成/图生视频/口播说唱唱歌电商讲解｜MiniMax H3自动数字人_2091192351791341570.json, 视频生成/图生视频/开源数字人自动版｜MiniMax-H3唱歌说唱口播讲解_2093766167809843202.json, 视频生成/图生视频/开源数字人｜MiniMax H3唱歌说唱口播全能，虚拟主播自动生成_2099920276535463937.json, 视频生成/图生视频/数字人唱歌说唱口播｜MiniMax-H3开源虚拟主播电商讲解自动版_2095554696181272577.json, 视频生成/图生视频/数字人唱歌说唱口播｜MiniMax-H3开源虚拟主播讲解_2093436709731127298.json, 视频生成/图生视频/数字人自动版｜MiniMax-H3唱歌说唱口播虚拟主播产品讲解_2089792313785675777.json, 视频生成/图生视频/虚拟主播电商产品讲解｜MiniMax-H3开源数字人唱歌说唱自动版_2095556325643210753.json, 视频生成/文生视频/MiniMaxH3多图数字人生成｜文生视频多图驱动_2094504932195000321.json, 视频生成/文生视频/多图数字人生成｜MiniMaxH3文生图生视频工作流_2094729429032464385.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_32

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/H3多图数字人最新优化版 多图参考数字人视频生成_2099199642356510721.json、视频生成/图生视频/MiniMax H3多图参考数字人唱歌精准对话 数字人口播方案_2109353184165715970.json、视频生成/图生视频/MiniMax H3开源数字人唱歌说唱口播虚拟主播电商产品讲解自动版工作流_2107966601273372673.json、视频生成/图生视频/MiniMax H3极速多参视频制作，文生视频图生视频多模式高效出片_2114423427422576642.json、视频生成/图生视频/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解角色设计_2090077928905330689.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
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
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 17/20 个有
- `AudioCrop` —— 17/20 个有
- `AudioSeparation` —— 17/20 个有
- `MathExpression|pysssss` —— 17/20 个有
- `ShowText|pysssss` —— 17/20 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 17/20 个有
- `llama_cpp_instruct_adv` —— 17/20 个有
- `llama_cpp_model_loader` —— 17/20 个有
- `llama_cpp_parameters` —— 17/20 个有
- `ComfyMathExpression` —— 14/20 个有
- `GetNode` —— 14/20 个有
- `PrimitiveFloat` —— 14/20 个有
- `SetNode` —— 14/20 个有
- `SaveText` —— 11/20 个有
- `Fast Groups Bypasser (rgthree)` —— 9/20 个有
- `easy float` —— 6/20 个有
- `SaveImage` —— 5/20 个有
- `CR Text` —— 3/20 个有
- `H3SigmaRefiner` —— 3/20 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 3/20 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 3/20 个有
- `ModelPreviewOverrideKJ` —— 3/20 个有
- `VAEDecodeAudio` —— 3/20 个有
- `VHS_LoadVideo` —— 3/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
