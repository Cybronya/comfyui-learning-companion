---
name: unknown_workflow_lora_sampler_unet_53
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5009
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/128.用Minimax H3+360度环绕lora+Skill做动态故事板，动态漫画，高级分镜视频_2109941253944201218.json, 图片生成/图生图/H3_终极篇-文武双全短剧-广告通用_2114203657913856001.json, 图片生成/图生图/MiniMax_H3_终极视频生成_多模态+提示词加强_高清加速工作流_2114254930012889090.json, 图片生成/图生图/YZ金鱼-MiniMax H3 终极篇-文武双全_2113256076882825218.json, 视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json, 视频生成/图生视频/YZ金鱼-MiniMax H3 终极篇-文武双全_2113823810985226242.json, 视频生成/图生视频/YZ金鱼-MiniMax H3 终极篇-文武双全_2113860678867046402.json, 视频生成/图生视频/文武双全首尾帧_2112932870200320002.json, 视频生成/图生视频/自己用的_2110993734681841665.json, 视频生成/图生视频/自用YZ金鱼-MiniMax H3 终极篇-文武双全_2110932091864174593.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_53

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/128.用Minimax H3+360度环绕lora+Skill做动态故事板，动态漫画，高级分镜视频_2109941253944201218.json、图片生成/图生图/H3_终极篇-文武双全短剧-广告通用_2114203657913856001.json、图片生成/图生图/MiniMax_H3_终极视频生成_多模态+提示词加强_高清加速工作流_2114254930012889090.json、图片生成/图生图/YZ金鱼-MiniMax H3 终极篇-文武双全_2113256076882825218.json、视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockSparseAttention` —— 9/10 个有
- `GetNode` —— 9/10 个有
- `GoohaiUniversalSlider` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `ModelPreviewOverrideKJ` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `Text` —— 9/10 个有
- `忽略多组孤海` —— 9/10 个有
- `VHS_VideoCombine` —— 8/10 个有
- `VHS_LoadVideo` —— 7/10 个有
- `MiniMaxChunkFeedForward` —— 5/10 个有
- `CM_FloatToInt` —— 2/10 个有
- `CreateVideo` —— 2/10 个有
- `GetVideoComponents` —— 2/10 个有
- `LoadVideo` —— 2/10 个有
- `MiniMaxH3PromptEnhancerT8` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `SaveVideo` —— 2/10 个有
- `ShowAnything|Mie` —— 2/10 个有
- `T8SpeechReference` —— 2/10 个有
- `ZNGB_AudioConcatMulti` —— 2/10 个有
- `ExtendIntermediateSigmas` —— 1/10 个有
- `MiniMaxH3AddGuide` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有
- `Vignette` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
