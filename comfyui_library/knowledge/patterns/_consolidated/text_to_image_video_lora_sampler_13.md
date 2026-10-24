---
name: text_to_image_video_lora_sampler_13
type: Text To Image
frequency: 30
level: strong
coverage: 0.621867
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3 全参官方指南｜自动扩展提示词 T7 实测_2096823650333843458.json, 图片生成/图生图/MiniMax H3全参官方指南自动扩展提示词视频处理工具_2101006979501215745.json, 图片生成/图生图/minimaxh3全参官方指南T7｜自动扩展提示词视频处理_2100784150339997697.json, 图片生成/图生图/全参官方指南T7｜minimaxh3自动扩展提示词处理_2093240407831437313.json, 图片生成/文生图/MiniMax H3 Ref2VA六图多参考角色一致性Sage加速文生图_2088251941397815297.json, 图片生成/文生图/文生视频 MiniMax H3_2097845481618624513.json, 数字人/数字人/Minimax H3多参考口播｜数字人口播素材多路喂｜口型和画面都对得上_2102653513489805313.json, 数字人/数字人/优化版本新版口播方案，数字人视频生视频制作_2111284544136630274.json, 数字人/数字人/新版口播数字人视频生成工作流｜视频生视频一键出片_2108369479599218690.json, 视频生成/图生视频/4步加速Lora二采高清放大｜H3全能参考图生视频画质增强_2088721636932538369.json, 视频生成/图生视频/4步加速Lora｜H3全能参考二采高清放大图生视频_2089065029676134402.json, 视频生成/图生视频/720P MiniMax H3超级多合一官方版｜图生视频工作流_2094857234391064577.json, 视频生成/图生视频/H3 Model High-Speed  美女模特图生视频直出 H3模型高速生成视频_2094945625723985922.json, 视频生成/图生视频/H3全能参考二采放大 图生视频高质量输出_2098282282468601858.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2090298920558747649.json, 视频生成/图生视频/H3模型 图生视频直出｜高速生成视频一键出片_2091428235719565313.json, 视频生成/图生视频/H3超级多合一工作流官方版 全功能视频生成_2100278481891450882.json, 视频生成/图生视频/MINIMAX-H3全能参考去油防脸崩-视频生视频图生视频_2087370270070886402.json, 视频生成/图生视频/MiniMax H3超级多合一官方版工作流｜多模式视频生成_2094500712767115265.json, 视频生成/图生视频/MiniMax H3超级多合一工作流官方版｜全能参考生成_2094499255737208833.json, 视频生成/图生视频/全能参考去油防MINIMAX-H3脸崩工作流ENG_2087124608590901249.json, 视频生成/图生视频/双采去水印版多图参考｜MiniMax H3视频生成直出_2093427385231302657.json, 视频生成/图生视频/双采去水印版｜MiniMax H3多图参考图生视频生成_2093758899559165953.json, 视频生成/图生视频/图生视频直出｜H3模型gy定制流 高速生成视频一键出片_2089422856018030594.json, 视频生成/图生视频/多参考API用｜MiniMax H3工作流图生视频生成_2089482490334498817.json, 视频生成/图生视频/官方本地版文图音频视频生视频二次高清放大｜MiniMax H3关闭二阶图生视频_2088161682400047105.json, 视频生成/图生视频/官方版本二次高清放大视频视频）生视频音频图H3（文MiniMax_2087327299141197825.json, 视频生成/图生视频/超级多合一官方V2｜MiniMax H3场景特效图生视频_2089454565593804802.json, 视频生成/文生视频/GSMiniMaxH3多参二次采样放大工作流ENGENG高尚ENG_2087137351121326082.json, 视频生成/文生视频/超级多合一官方版V2文生图生视频｜MiniMax H3视频生成工作流_2088317993481760769.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/图生图/MiniMax H3 全参官方指南｜自动扩展提示词 T7 实测_2096823650333843458.json、图片生成/图生图/MiniMax H3全参官方指南自动扩展提示词视频处理工具_2101006979501215745.json、图片生成/图生图/minimaxh3全参官方指南T7｜自动扩展提示词视频处理_2100784150339997697.json、图片生成/图生图/全参官方指南T7｜minimaxh3自动扩展提示词处理_2093240407831437313.json、图片生成/文生图/MiniMax H3 Ref2VA六图多参考角色一致性Sage加速文生图_2088251941397815297.json…）

- **类型**：Text To Image
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 30 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 29/30 个有
- `Text` —— 28/30 个有
- `孤海注释` —— 28/30 个有
- `GetNode` —— 26/30 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 26/30 个有
- `SetNode` —— 26/30 个有
- `MiniMaxH3ReferenceToVideo` —— 25/30 个有
- `PreviewImage` —— 24/30 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 23/30 个有
- `ImageResizeKJv2` —— 21/30 个有
- `VAEEncode` —— 21/30 个有
- `LoadAudio` —— 20/30 个有
- `VAEDecodeAudio` —— 20/30 个有
- `VHS_LoadVideo` —— 20/30 个有
- `VAEEncodeAudio` —— 19/30 个有
- `Fast Groups Bypasser (rgthree)` —— 18/30 个有
- `PT_H3ConcatAVLatent` —— 14/30 个有
- `ModelAttentionBackend` —— 11/30 个有
- `easy cleanGpuUsed` —— 11/30 个有
- `MiniMaxH3AVDecodeT8` —— 10/30 个有
- `MiniMaxH3ImageToVideo` —— 8/30 个有
- `RunningHub Deepcleaner` —— 8/30 个有
- `LTXVConcatAVLatent` —— 7/30 个有
- `PathchSageAttentionKJ` —— 6/30 个有
- `ImageConcatenateMulti_UTK` —— 4/30 个有
- `RHHiddenNodes` —— 4/30 个有
- `SaveImage` —— 4/30 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 4/30 个有
- `MiniMaxH3AddGuide` —— 3/30 个有
- `CR Prompt Text` —— 2/30 个有
- `LoraLoaderBypassModelOnly` —— 2/30 个有
- `SaveVideo` —— 2/30 个有
- `CRTFirstLastFrameSelector` —— 1/30 个有
- `EmptyImage` —— 1/30 个有
- `TrimAudioDuration` —— 1/30 个有
- `VHS_LoadVideoFFmpeg` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 30 | 100% |
| 高度 | 80 | 80 - 80 | 30 | 100% |
| 采样步数 | 4 | 4 - 4 | 30 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 30 | 100% |
| 采样算法 | er_sde | - | 30 | 100% |
| 调度器 | beta | - | 30 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 30 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 31/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，30 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，30 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，30 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，30 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，30 个样本，一致性 100%
- 调度器 最常用 beta，30 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，30 个样本，取值集中（一致性 100%）
- 高发问题（31/30 个样本）：Steps较低可能导致细节不足
