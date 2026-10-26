---
name: text_to_image_lora_sampler_clip_17
type: Text To Image
frequency: 29
level: strong
coverage: 0.893034
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json, 视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json, 视频生成/图生视频/8步加速首帧参考｜MiniMax H3写实图生视频战斗特效_2089381704552247298.json, 视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json, 视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098819339918073857.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2098820909527293953.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099181667595407361.json, 视频生成/图生视频/H3首尾帧官方提示词指南自动扩写 角色一致性分镜生成_2099549898831126529.json, 视频生成/图生视频/MInimaxH3首尾帧T3指南｜官方提示词自动扩写，分镜出图更对味_2099427468598923266.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T7版｜自动扩写保角色一致性｜分镜出图_2099115888204140545.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南T8升级版｜自动扩写分镜一致出片_2099117086592290817.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南自动扩写_2086206535667109889.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T2分镜更稳_2106263717989150721.json, 视频生成/图生视频/MInimaxH3首尾帧官方提示词指南｜自动扩写T3分镜出图_2106974045374869506.json, 视频生成/图生视频/MiniMax H3首尾帧参考生成 官方提示词自动扩写T2_2098110557789446146.json, 视频生成/图生视频/T2首尾帧官方指南｜MInimaxH3提示词自动扩写生成_2094777866826371074.json, 视频生成/图生视频/T3官方指南首尾帧｜MInimaxH3提示词自动扩写分镜_2095062492773961730.json, 视频生成/图生视频/T7官方指南首尾帧｜MInimaxH3提示词自动扩写分镜出图_2094772557869309953.json, 视频生成/图生视频/T8官方指南首尾帧｜MInimaxH3提示词自动扩写出图_2095070966761213953.json, 视频生成/图生视频/人物微表情变化｜图生视频捕捉眨眼抿嘴 细节拉满_2097850526296797185.json, 视频生成/图生视频/人物表情变化动作生成｜图生视频形象动态演绎工作流_2097536720039399426.json, 视频生成/图生视频/人物表情变化动作｜图生视频让静态人像笑起来动起来_2097522798133596161.json, 视频生成/图生视频/图生视频｜MiniMax H3 8步加速首帧参考生视频 写实战斗特效_2089244304341561345.json, 视频生成/图生视频/官方提示词指南自动扩写T1｜MInimaxH3首尾帧图生视频_2095791903588569089.json, 视频生成/图生视频/提示词指南自动扩写T7｜MinimaxH3首尾帧分镜出图_2091166611460939778.json, 视频生成/图生视频/美好的夏天｜图生视频把夏日照片变成会动的回忆短片_2097543142554820609.json, 视频生成/文生视频/H3六步文生视频短片预检版 开源加速采样工作流_2098840495605764097.json, 视频生成/文生视频/H3六步文生视频短片预检版｜六步走完从想法到成片_2099146163709628418.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（数字人/数字人/开源版问生视频H3加速Lora6步直出1080PMinimax_2086207991736528898.json、视频生成/图生视频/1080高画质动作迁移｜MinimaxH3 Easy人物服装替换全注释_2093428928621932546.json、视频生成/图生视频/8步加速首帧参考｜MiniMax H3写实图生视频战斗特效_2089381704552247298.json、视频生成/图生视频/Easy动作迁移1080高画质｜MinimaxH3 角色服装替换全节点注释_2089271413906698242.json、视频生成/图生视频/Easy稳定性优化1080｜MinimaxH3动作迁移人物服装替换_2093760414810206210.json…）

- **类型**：Text To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 29 个 workflow 都包含：
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
- `孤海注释` —— 28/29 个有
- `LoadImage` —— 26/29 个有
- `VHS_VideoCombine` —— 26/29 个有
- `ComfyMathExpression` —— 23/29 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 23/29 个有
- `MiniMaxH3ImageToVideo` —— 23/29 个有
- `PrimitiveFloat` —— 23/29 个有
- `easy showAnything` —— 23/29 个有
- `Text` —— 21/29 个有
- `ImageResizeKJv2` —— 20/29 个有
- `RHHiddenNodes` —— 16/29 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/29 个有
- `SaveImage` —— 7/29 个有
- `MiniMaxH3Easy` —— 6/29 个有
- `MiniMaxH3EasyLoader` —— 6/29 个有
- `MiniMaxH3EasyOutput` —— 6/29 个有
- `RH_Captioner` —— 6/29 个有
- `CreateVideo` —— 5/29 个有
- `PathchSageAttentionKJ` —— 5/29 个有
- `SaveVideo` —— 5/29 个有
- `TextConcatenate_UTK` —— 5/29 个有
- `MiniMaxH3BlockCacheT8` —— 4/29 个有
- `CR Text` —— 3/29 个有
- `LoadVideo` —— 3/29 个有
- `MiniMaxH3SigmaShift` —— 3/29 个有
- `BiRefNetRMBG` —— 2/29 个有
- `PrimitiveStringMultiline` —— 2/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 29 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 29 | 100% |
| 采样算法 | er_sde | - | 29 | 100% |
| 调度器 | beta | - | 29 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |
| 宽度 | 80 | 80 - 80 | 29 | 100% |
| 高度 | 80 | 80 - 80 | 29 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，29 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，29 个样本，一致性 100%
- 调度器 最常用 beta，29 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，29 个样本，取值集中（一致性 100%）
- 高发问题（29/29 个样本）：Steps较低可能导致细节不足
