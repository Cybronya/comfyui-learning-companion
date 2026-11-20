---
name: text_to_image_video_lora_sampler_14
type: Text To Image
frequency: 28
level: strong
coverage: 0.645929
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax-H3开源多图生视频｜数字人视频带货电商口播好帮手_2104534112320180225.json, 视频生成/图生视频/MiniMax-H3开源数字人视频带货｜多图生视频电商口播神器_2104495131775815681.json, 视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json, 视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json, 视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars电商好帮手_2111119123915821058.json, 视频生成/图生视频/MiniMaxH3 ref2va加速八步采样-图生视频工作流_2087367770194403330.json, 视频生成/图生视频/MiniMaxH3 ref2va四步加速V4版｜图生视频_2090101812916482049.json, 视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2089456017561186306.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速版_2091266588484923394.json, 视频生成/图生视频/ref2va四步加速v4｜MiniMaxH3图生视频极速直出_2089807243888914434.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3图生视频1.0分辨率极速出片_2093095662807248897.json, 视频生成/图生视频/ref2va超级加速版｜MiniMaxH3支持1.0分辨率图生视频_2093253169697611778.json, 视频生成/图生视频/多图参考带货视频｜MiniMax-H3数字人倾情出镜_2096572891126124546.json, 视频生成/图生视频/开源多参考优化版｜MiniMax H3角色一致性生视频_2094474289755021314.json, 视频生成/图生视频/数字人视频带货｜MiniMax-H3多图参考生视频制作_2096314183389372417.json, 视频生成/文生视频/H3最强双采FL2-736P高清PRO焚诀展开篇｜文生视频视频生视频图生视频全链路_2100454010141626369.json, 视频生成/文生视频/Jason二采H3多参考生视频优化版V2｜三模式视频生成_2108420583481499650.json, 视频生成/文生视频/Jason二采H3多参考生视频优化版｜不油腻二采高清放大更耐看_2101906733156364290.json, 视频生成/文生视频/MiniMax H3 全能视频生成｜文生图生视频多合一极速二采优化_2097497016648683521.json, 视频生成/文生视频/MiniMax H3多参考7P3A2V二采优化版｜多素材混合生视频，画面节奏更耐看_2100487458340294657.json, 视频生成/文生视频/MiniMax H3多参考7P3A2V生视频优化版｜文生视频视频生视频全都能接_2100485687203155970.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜文生视频图生视频画质更稳_2104532274321645569.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜文生视频视频生视频_2106990754123051010.json, 视频生成/文生视频/MiniMax H3多参考生视频优化版｜高质量生成_2095587743173799938.json, 视频生成/文生视频/MiniMax H3多参考生视频｜优化版高质量生成_2095226419768029186.json, 视频生成/文生视频/MiniMax H3多图多音频视频参考｜无水印优化版_2095227965956247554.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_14

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/MiniMax-H3开源多图生视频｜数字人视频带货电商口播好帮手_2104534112320180225.json、视频生成/图生视频/MiniMax-H3开源数字人视频带货｜多图生视频电商口播神器_2104495131775815681.json、视频生成/图生视频/MiniMax-H3数字人带货图生视频_2108450739797446658.json、视频生成/图生视频/MiniMax-H3数字人带货视频｜模特产品展示图生视频_2108417540744638465.json、视频生成/图生视频/MiniMax-H3数字人视频带货｜Digital Avatars模特产品展示_2108393078053756930.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 27/28 个有
- `孤海注释` —— 27/28 个有
- `KSamplerSelect` —— 22/28 个有
- `LTXVConcatAVLatent` —— 20/28 个有
- `LTXVSeparateAVLatent` —— 20/28 个有
- `LoadAudio` —— 20/28 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 20/28 个有
- `MinimaxH3LatentUpscaler3D` —— 20/28 个有
- `VHS_LoadVideo` —— 13/28 个有
- `SplitSigmas` —— 12/28 个有
- `Text` —— 11/28 个有
- `easy float` —— 11/28 个有
- `ManualSigmas` —— 8/28 个有
- `Text Multiline` —— 8/28 个有
- `ModelPatchTorchSettings` —— 7/28 个有
- `ImageScale` —— 6/28 个有
- `MiniMaxH3TurboLoRA` —— 6/28 个有
- `MiniMaxH3TurboSampler` —— 6/28 个有
- `PrimitiveInt` —— 6/28 个有
- `easy compare` —— 6/28 个有
- `忽略多组孤海` —— 3/28 个有
- `Label (rgthree)` —— 2/28 个有
- `Fast Groups Bypasser (rgthree)` —— 1/28 个有
- `FloatConstant` —— 1/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/28 个有
- `PreviewImage` —— 1/28 个有
- `easy clearCacheAll` —— 1/28 个有
- `图像缩放范围孤海` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| 宽度 | 80 | 80 - 80 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
