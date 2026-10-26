---
name: text_to_image_video_lora_sampler_39
type: Text To Image
frequency: 18
level: strong
coverage: 0.872611
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyOutput, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json, 视频生成/图生视频/Minimax H3-Easy多图叙事 视频运镜慢剧生成工具_2113758475133210626.json, 视频生成/图生视频/Minimax H3-Easy多图叙事慢剧｜运镜细腻图生视频故事感_2113512909535014913.json, 视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换｜1080高画质服装替换全注释_2089453564925136898.json, 视频生成/图生视频/MinimaxH3 Easy角色服装替换动作迁移｜1080高画质全节点注释视频生视频_2089719236200583170.json, 视频生成/图生视频/MinimaxH3视频生成工作台 支持图片参考多图创作_2098713051313819650.json, 视频生成/图生视频/MinimaxH3视频生成工作台｜支持@图片直接驱动_2098702232026963970.json, 视频生成/图生视频/全模式精简流独立双采样｜MINIMAX-H3开源最强去油_2095831597303025666.json, 视频生成/图生视频/参考图生视频生成｜MiniMaxH3高质量出片工作流_2095049456667414529.json, 视频生成/图生视频/最强去油全模式精简流｜MINIMAX-H3开源独立双采样_2095828211811835906.json, 视频生成/文生视频/H3台词优化多合一极简版工作流 视频生成处理_2100665823122780162.json, 视频生成/文生视频/H3提示词Skills V2.5优化台词多合一极简版，文生视频图生视频方案_2103960622621872129.json, 视频生成/文生视频/MiniMax H3极简流分块二采，支持种子固定的文生视频图生视频方案_2103191478523752449.json, 视频生成/文生视频/MiniMax_H3全模式双采样｜精简流优化版生成_2095278240096145410.json, 视频生成/文生视频/Minimax H3多参单采优化兼顾速度质量与打斗 视频生成均衡版_2105413868599205889.json, 视频生成/文生视频/Minimax-H3多参单采优化｜速度质量打斗场面三兼顾_2105131373353848833.json, 视频生成/文生视频/MinimaxH3大全自动高清VOSR DLSS增强 数字人文生视频工具_2098656335591198721.json, 视频生成/文生视频/海螺H3多模型合一 自动高清VOSR加DLSS超分辨率视频增强_2098651454662860801.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_39

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3参考图生视频｜角色一致性视频生成_2095091404421820417.json、视频生成/图生视频/Minimax H3-Easy多图叙事 视频运镜慢剧生成工具_2113758475133210626.json、视频生成/图生视频/Minimax H3-Easy多图叙事慢剧｜运镜细腻图生视频故事感_2113512909535014913.json、视频生成/图生视频/MinimaxH3 Easy动作迁移人物替换｜1080高画质服装替换全注释_2089453564925136898.json、视频生成/图生视频/MinimaxH3 Easy角色服装替换动作迁移｜1080高画质全节点注释视频生视频_2089719236200583170.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyOutput`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LTXVConcatAVLatent` —— 12/18 个有
- `LTXVSeparateAVLatent` —— 12/18 个有
- `MinimaxH3LatentUpscaler3D` —— 12/18 个有
- `SplitSigmas` —— 12/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 11/18 个有
- `Fast Groups Bypasser (rgthree)` —— 10/18 个有
- `LoadAudio` —— 10/18 个有
- `MiniMaxH3EasyLoader` —— 10/18 个有
- `H3SigmaRefiner` —— 8/18 个有
- `MiniMaxH3EasyModelAdapter` —— 8/18 个有
- `MiniMaxH3EasySecondPassConditioning` —— 8/18 个有
- `SaveImage` —— 8/18 个有
- `LoadImage` —— 7/18 个有
- `ModelAttentionBackend` —— 7/18 个有
- `LoadVideo` —— 6/18 个有
- `MiniMaxH3EasyMediaLoader` —— 5/18 个有
- `PrimitiveInt` —— 4/18 个有
- `SetNode` —— 4/18 个有
- `VHS_LoadVideo` —— 4/18 个有
- `GoohaiMinimaxH3TiledSampler` —— 3/18 个有
- `CR Text` —— 2/18 个有
- `GetNode` —— 2/18 个有
- `GoohaiAnyExists` —— 2/18 个有
- `IfInnerExecute` —— 2/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/18 个有
- `ModelPreviewOverrideKJ` —— 2/18 个有
- `PDIMAGE_LongerSize` —— 2/18 个有
- `PreviewImage` —— 2/18 个有
- `PrimitiveStringMultiline` —— 2/18 个有
- `RH_DLSS5Enhance` —— 2/18 个有
- `RTXVideoSuperResolution` —— 2/18 个有
- `TextInput_` —— 2/18 个有
- `VOSR2ModelLoader` —— 2/18 个有
- `VOSR2Upscale` —— 2/18 个有
- `easy cleanGpuUsed` —— 2/18 个有
- `Seed (rgthree)` —— 1/18 个有
- `Text` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
