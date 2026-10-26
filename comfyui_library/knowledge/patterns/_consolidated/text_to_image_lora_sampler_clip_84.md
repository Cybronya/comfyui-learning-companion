---
name: text_to_image_lora_sampler_clip_84
type: Text To Image
frequency: 14
level: strong
coverage: 0.869
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json, 图片生成/图生图/MiniMax H3参考生视频量化加速版多模态处理工具_2101367524666470402.json, 图片生成/图生图/MiniMax H3视频换装带货展示，动作迁移服装呈现_2110826055559892993.json, 图片生成/图生图/MiniMaxH3参考生视频量化加速版｜文本图像音频视频多模态_2101210370760335362.json, 图片生成/图生图/Minimax H3单人版人物替换｜自动反推提示词免手写｜一键视频换人_2112064275526279169.json, 图片生成/图生图/PR插件专用｜AI Video Studio短剧生成加速优化版直出_2089798943013167106.json, 图片生成/图生图/单人人物替换自动反推，Minimax H3动作迁移图生图_2112250764386193410.json, 数字人/数字人/9参考MINIMAX-H3数字人_2086538496143089666.json, 视频生成/图生视频/H3开源 动作迁移一键复刻｜MiniMaxH3图生视频舞蹈复制动作复刻_2092940607059746817.json, 视频生成/图生视频/人物替换单人稳定版｜Minimax H3图生视频工作流_2087216847925104641.json, 视频生成/图生视频/动作迁移单人稳定版｜Minimax H3图生视频工作流_2087226692820619265.json, 视频生成/图生视频/动作迁移单人稳定版｜Minimax H3图生视频工作流_2092982995232845825.json, 视频生成/图生视频/图生视频工作流Minimax H3单人稳定版动作迁移高效首选_2089319411319664642.json, 视频生成/图生视频/图生视频工作流Minimax H3单人稳定版动作迁移高效首选_2091760129564831746.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/MiniMax H3加速版AI Video Studio PR插件｜VIP专用短剧生成优化版_2090085975216189442.json、图片生成/图生图/MiniMax H3参考生视频量化加速版多模态处理工具_2101367524666470402.json、图片生成/图生图/MiniMax H3视频换装带货展示，动作迁移服装呈现_2110826055559892993.json、图片生成/图生图/MiniMaxH3参考生视频量化加速版｜文本图像音频视频多模态_2101210370760335362.json、图片生成/图生图/Minimax H3单人版人物替换｜自动反推提示词免手写｜一键视频换人_2112064275526279169.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 12/14 个有
- `PrimitiveStringMultiline` —— 12/14 个有
- `ResolutionSelector` —— 12/14 个有
- `孤海注释` —— 12/14 个有
- `VHS_LoadVideo` —— 11/14 个有
- `JoinStrings` —— 10/14 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/14 个有
- `SaveVideo` —— 10/14 个有
- `EasyCache` —— 8/14 个有
- `Bjornulf_ShowFloat` —— 7/14 个有
- `PrimitiveFloat` —— 7/14 个有
- `RH_LLMAPI_Pro_Node` —— 7/14 个有
- `VHS_VideoInfoLoaded` —— 7/14 个有
- `easy showAnything` —— 7/14 个有
- `LoadAudio` —— 4/14 个有
- `PathchSageAttentionKJ` —— 4/14 个有
- `VHS_VideoCombine` —— 4/14 个有
- `SaveImage` —— 3/14 个有
- `AILab_QwenVL` —— 2/14 个有
- `CR Prompt Text` —— 2/14 个有
- `DF_Int_to_Float` —— 2/14 个有
- `ImageConcanate` —— 2/14 个有
- `ImageResizeKJv2` —— 2/14 个有
- `ImageUpscaleWithModel` —— 2/14 个有
- `PrimitiveInt` —— 2/14 个有
- `UpscaleModelLoader` —— 2/14 个有
- `JWString` —— 1/14 个有
- `LoadVideo` —— 1/14 个有
- `LoraLoaderBypassModelOnly` —— 1/14 个有
- `VideoFrameSelector` —— 1/14 个有
- `easy imageRemBg` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
