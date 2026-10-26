---
name: text_to_image_video_lora_sampler_63
type: Text To Image
frequency: 12
level: strong
coverage: 0.514833
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, GetImage, GetNode, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, PreviewAudio, PreviewImage, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, ResolutionSelector, SetNode, StringConcatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, YUAN_TXTJsonExtractor, YUAN_TXTJsonSwitch, YUAN_TXTPreviewContent, YUAN_TXTShotDurations, YuanAudioList, YuanAudioLoad, YuanAudioSplit, YuanMultiImage, YuanTool, Yuan_MiniMaxH3Video, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3全栈式文武戏短剧 SelfLift双模生成工具_2114117923668324354.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成V12.1宫格版，图生视频短剧制作工具_2106106643212750849.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作工具_2098655909403783169.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成宫格版 图生视频CG幻想风格多场景产出_2105443312898498561.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成宫格版，图生视频CG幻想风格多场景产出_2102902512931135489.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成宫格版，图生视频短剧制作工具_2107181508682407938.json, 视频生成/图生视频/MiniMax H3全栈式短剧生成短剧版，图生视频一站式短剧制作工作流_2102904045089411073.json, 视频生成/图生视频/MiniMax-H3全栈式短剧生成V12.1宫格版｜图生视频短剧利器_2106989222166097922.json, 视频生成/图生视频/MiniMax_H3全栈式短剧生成宫格版，图生视频CG幻想风格多场景产出_2104734396803796994.json, 视频生成/图生视频/MiniMax_H3全栈式短剧生成宫格版，图生视频短剧制作工具_2109442367852994561.json, 视频生成/文生视频/MiniMax_H3全栈式短剧生成短剧版，图生视频一站式短剧制作工作流_2104732928919031809.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3全栈式文武戏短剧 SelfLift双模生成工具_2114117923668324354.json、视频生成/图生视频/MiniMax H3全栈式短剧生成V12.1宫格版，图生视频短剧制作工具_2106106643212750849.json、视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作_2098294284297527297.json、视频生成/图生视频/MiniMax H3全栈式短剧生成V9.2 一站式短剧制作工具_2098655909403783169.json、视频生成/图生视频/MiniMax H3全栈式短剧生成宫格版 图生视频CG幻想风格多场景产出_2105443312898498561.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PreviewAudio`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SetNode`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `YUAN_TXTJsonExtractor`
- `YUAN_TXTJsonSwitch`
- `YUAN_TXTPreviewContent`
- `YUAN_TXTShotDurations`
- `YuanAudioList`
- `YuanAudioLoad`
- `YuanAudioSplit`
- `YuanMultiImage`
- `YuanTool`
- `Yuan_MiniMaxH3Video`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 11/12 个有
- `孤海注释` —— 10/12 个有
- `Fast Groups Bypasser (rgthree)` —— 8/12 个有
- `LoadImage` —— 8/12 个有
- `ResizeImageMaskNode` —— 8/12 个有
- `VOSR2ModelLoader` —— 8/12 个有
- `VOSR2Upscale` —— 8/12 个有
- `YuanImageGridComposite` —— 8/12 个有
- `YuanLoadImageOutput` —— 8/12 个有
- `YuanPrimitive` —— 8/12 个有
- `Yuan_H3MotionContextTrim` —— 8/12 个有
- `Yuan_H3ProgressiveSampler` —— 8/12 个有
- `BasicGuider` —— 4/12 个有
- `EmptyImage` —— 4/12 个有
- `ImageFromBatch` —— 4/12 个有
- `Lora Loader Stack (rgthree)` —— 4/12 个有
- `ManualSigmas` —— 4/12 个有
- `MiniMaxH3AddGuide` —— 4/12 个有
- `RandomNoise` —— 4/12 个有
- `SamplerCustomAdvanced` —— 4/12 个有
- `SplitSigmas` —— 4/12 个有
- `StringReplace` —— 4/12 个有
- `VAEDecodeAudio` —— 4/12 个有
- `Yuan_H3Upscale3D` —— 4/12 个有
- `Yuan_VideoUI` —— 4/12 个有
- `easy clearCacheAll` —— 3/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
