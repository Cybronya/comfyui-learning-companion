---
name: text_to_image_lora_sampler_clip_21
type: Text To Image
frequency: 19
level: strong
coverage: 0.901105
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频首尾帧控制｜原生音频自带，两张图变一段电影感短片_2100451183075880961.json, 视频生成/图生视频/MiniMax H3图生视频首尾帧视频二采加速版 高质量动态生成_2105373937122242561.json, 视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json, 视频生成/图生视频/MiniMax H3多图参考生成视频，图生视频与视频生视频全能参考方案_2102813018273968130.json, 视频生成/图生视频/MiniMax H3多图参考生视频图生视频处理生成工具_2101745060818808833.json, 视频生成/图生视频/MiniMax H3多图参考生视频工作流_视频生视频图生视频多素材融合方案_2105760424162586626.json, 视频生成/图生视频/MiniMax H3多图参考生视频｜几张图一起喂｜人物场景一致性拉满_2102579245317967874.json, 视频生成/图生视频/MiniMax H3多图参考生视频｜多素材参考一致性视频生成_2108015949080260609.json, 视频生成/图生视频/MiniMax H3开源版首尾帧8步加速工作流_数字人图生视频处理工具_2106532091839205378.json, 视频生成/图生视频/MiniMax H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2106532091839205378.json, 视频生成/图生视频/MiniMax H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2106879845912371201.json, 视频生成/图生视频/MiniMax H3首尾帧3步快速生成图生视频处理工具_2101395032807923714.json, 视频生成/图生视频/MiniMax H3首尾帧二采加速版｜图生视频稳定出片_2105267559749734401.json, 视频生成/图生视频/MiniMax_H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2109819079400968194.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大工作流，文生视频视频生视频图生视频_2109816691227185154.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大，三种生视频模式_2110541129706987521.json, 视频生成/图生视频/MiniMax_H3多参角色替换LoRA二采放大，三种生视频模式_2110888174443655170.json, 视频生成/图生视频/h3 二阶+sigma+latent 采样组合｜数字人图生视频_2096896924396900353.json, 视频生成/文生视频/MiniMax H3单模双采放大工作流8G显存版，低显存笔记本也能跑方案_2106866016801345537.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_21

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频首尾帧控制｜原生音频自带，两张图变一段电影感短片_2100451183075880961.json、视频生成/图生视频/MiniMax H3图生视频首尾帧视频二采加速版 高质量动态生成_2105373937122242561.json、视频生成/图生视频/MiniMax H3多图参考生成视频图生视频与视频生视频全能参考方案_2107257293007052802.json、视频生成/图生视频/MiniMax H3多图参考生成视频，图生视频与视频生视频全能参考方案_2102813018273968130.json、视频生成/图生视频/MiniMax H3多图参考生视频图生视频处理生成工具_2101745060818808833.json…）

- **类型**：Text To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 19 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 16/19 个有
- `SaveImage` —— 14/19 个有
- `MiniMaxH3ReferenceToVideo` —— 12/19 个有
- `PrimitiveStringMultiline` —— 11/19 个有
- `LTXVConcatAVLatent` —— 9/19 个有
- `LTXVSeparateAVLatent` —— 9/19 个有
- `MinimaxH3LatentUpscaler3D` —— 9/19 个有
- `SplitSigmas` —— 9/19 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 8/19 个有
- `MiniMaxH3ImageToVideo` —— 7/19 个有
- `MiniMaxH3SigmaShift` —— 7/19 个有
- `ModelAttentionBackend` —— 7/19 个有
- `ModelPreviewOverrideKJ` —— 7/19 个有
- `EmptyImage` —— 6/19 个有
- `LoadAudio` —— 6/19 个有
- `PreviewImage` —— 6/19 个有
- `VHS_VideoCombine` —— 5/19 个有
- `ImageResizeKJv2` —— 4/19 个有
- `ManualSigmas` —— 4/19 个有
- `ExtendIntermediateSigmas` —— 3/19 个有
- `Fast Groups Bypasser (rgthree)` —— 3/19 个有
- `Text` —— 3/19 个有
- `VHS_LoadVideo` —— 3/19 个有
- `easy showAnything` —— 3/19 个有
- `PathchSageAttentionKJ` —— 2/19 个有
- `easy getNode` —— 2/19 个有
- `easy int` —— 2/19 个有
- `easy loraStack` —— 2/19 个有
- `easy loraStackApply` —— 2/19 个有
- `easy setNode` —— 2/19 个有
- `CR Text` —— 1/19 个有
- `Fast Groups Muter (rgthree)` —— 1/19 个有
- `GetImageSize` —— 1/19 个有
- `ImageConcatMulti` —— 1/19 个有
- `RH_LLMAPI_Pro_Node` —— 1/19 个有
- `SolAttnMiniMax` —— 1/19 个有
- `TextOverlay` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 19 | 100% |
| 高度 | 80 | 80 - 80 | 19 | 100% |
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 19 | 100% |
| 采样算法 | er_sde | - | 19 | 100% |
| 调度器 | beta | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，19 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，19 个样本，一致性 100%
- 调度器 最常用 beta，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（23/19 个样本）：Steps较低可能导致细节不足
