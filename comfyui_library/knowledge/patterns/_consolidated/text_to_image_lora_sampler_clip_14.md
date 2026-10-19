---
name: text_to_image_lora_sampler_clip_14
type: Text To Image
frequency: 21
level: strong
coverage: 0.894476
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json, 视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json, 视频生成/图生视频/8步加速首帧参考｜MiniMax H3写实图生视频战斗特效_2089381704552247298.json, 视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json, 视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098819339918073857.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098820909527293953.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099181667595407361.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099549898831126529.json, 视频生成/图生视频/MInimaxH3首尾帧T3指南｜官方提示词自动扩写，分镜出图更对味_2099427468598923266.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T7版｜自动扩写保角色一致性｜分镜出图_2099115888204140545.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T8升级版｜自动扩写分镜一致出片_2099117086592290817.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南_自动扩写T2分镜更稳_2106263717989150721.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南自动扩写_2086206535667109889.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T3分镜出图_2106974045374869506.json, 视频生成/图生视频/MiniMax H3首尾帧参考生成 官方提示词自动扩写T2_2098110557789446146.json, 视频生成/图生视频/MiniMaxH3首尾帧提示词指南T7｜自动扩写分镜出图_2094493855881187329.json, 视频生成/图生视频/MiniMaxH3首尾帧自动扩写｜官方提示词指南T1_2095564089794846721.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094250837928407041.json, 视频生成/图生视频/图生视频快速生成 Minimax H3 画质稳定出片_2094271866994257922.json, 视频生成/图生视频/图生视频｜MiniMax H3 8步加速首帧参考生视频 写实战斗特效_2089244304341561345.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json、视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json、视频生成/图生视频/8步加速首帧参考｜MiniMax H3写实图生视频战斗特效_2089381704552247298.json、视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json、视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 20/21 个有
- `VHS_VideoCombine` —— 20/21 个有
- `孤海注释` —— 20/21 个有
- `ComfyMathExpression` —— 17/21 个有
- `MiniMaxH3ImageToVideo` —— 17/21 个有
- `PrimitiveFloat` —— 17/21 个有
- `ImageResizeKJv2` —— 16/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/21 个有
- `easy showAnything` —— 15/21 个有
- `Text` —— 13/21 个有
- `RHHiddenNodes` —— 12/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/21 个有
- `SaveImage` —— 5/21 个有
- `MiniMaxH3Easy` —— 4/21 个有
- `MiniMaxH3EasyLoader` —— 4/21 个有
- `MiniMaxH3EasyOutput` —— 4/21 个有
- `CR Text` —— 3/21 个有
- `CreateVideo` —— 3/21 个有
- `LoadVideo` —— 3/21 个有
- `MiniMaxH3SigmaShift` —— 3/21 个有
- `PathchSageAttentionKJ` —— 3/21 个有
- `SaveVideo` —— 3/21 个有
- `BiRefNetRMBG` —— 2/21 个有
- `RH_Captioner` —— 2/21 个有
- `TextConcatenate_UTK` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 21 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 21 | 100% |
| 采样算法 | er_sde | - | 21 | 100% |
| 调度器 | beta | - | 21 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 21 | 100% |
| 宽度 | 80 | 80 - 80 | 21 | 100% |
| 高度 | 80 | 80 - 80 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，21 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，21 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，21 个样本，一致性 100%
- 调度器 最常用 beta，21 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，21 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，21 个样本，取值集中（一致性 100%）
- 高发问题（21/21 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
