---
name: unknown_workflow_lora_sampler_clip_54
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.565222
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadSAM2Model, DrawMaskOnImage, GrowMask, ImageBatch, ImageFromBatch, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PixelPerfectResolution, PointsEditor, PrimitiveInt, Sam2Segmentation, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, WanAnimateToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.2动作迁移工作流_2077008248456171521.json, 平台全量/Wan Animate视频角色替换_2058231696549568513.json, 平台全量/Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066.json, 平台全量/video_wan2_2_14B_animate_native_auto_extend_1971147916700225538.json, 平台全量/角色替换&动作迁移_2117046433357582337.json, 数字人/数字人/ComfyUI_电商视频_整人物替换_Wan2.2_Animate_2081230895100547074.json, 视频生成/图生视频/Wan Animate角色动作迁移_2058456295702876162.json, 视频生成/图生视频/Wan2_2_14B_Animate_自动循环-动作迁移_1973652058060533761.json, 视频生成/图生视频/video_wan2_2_14B_animate-移动模式_1971010678985265154.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/wan2.2动作迁移工作流_2077008248456171521.json、平台全量/Wan Animate视频角色替换_2058231696549568513.json、平台全量/Wan2.2 Animate把你变成山鸡哥，ComfyUI官方工作流详解_1970698443058520066.json、平台全量/video_wan2_2_14B_animate_native_auto_extend_1971147916700225538.json、平台全量/角色替换&动作迁移_2117046433357582337.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 9 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GrowMask`
- `ImageBatch`
- `ImageFromBatch`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PixelPerfectResolution`
- `PointsEditor`
- `PrimitiveInt`
- `Sam2Segmentation`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanAnimateToVideo`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/9 个有
- `MaskPreview` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `SaveVideo` —— 7/9 个有
- `GetNode` —— 6/9 个有
- `SetNode` —— 6/9 个有
- `GetVideoComponents` —— 5/9 个有
- `LoadVideo` —— 4/9 个有
- `MathExpression|pysssss` —— 4/9 个有
- `VHS_VideoCombine` —— 4/9 个有
- `ImageConcatMulti` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `Bjornulf_ShowInt` —— 2/9 个有
- `ForLoopClose` —— 2/9 个有
- `ForLoopOpen` —— 2/9 个有
- `ImageResizeKJv2` —— 2/9 个有
- `MaskToImage` —— 2/9 个有
- `VHS_LoadVideoFFmpeg` —— 2/9 个有
- `VHS_VideoInfo` —— 2/9 个有
- `VHS_VideoInfoLoaded` —— 2/9 个有
- `easy forLoopEnd` —— 2/9 个有
- `easy forLoopStart` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `Bjornulf_ShowFloat` —— 1/9 个有
- `ImageResizeAdvanced` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（21/9 个样本）：Steps较低可能导致细节不足
