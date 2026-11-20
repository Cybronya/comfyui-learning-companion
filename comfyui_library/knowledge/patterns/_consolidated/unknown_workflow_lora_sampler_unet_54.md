---
name: unknown_workflow_lora_sampler_unet_54
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.482091
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, ModelAttentionBackend, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/128.用Minimax H3+360度环绕lora+Skill做动态故事板，动态漫画，高级分镜视频_2109941253944201218.json, 图片生成/图生图/H3_终极篇-文武双全短剧-广告通用_2114203657913856001.json, 图片生成/图生图/H3_终极篇-文武双全短剧-广告通用_2115242482991722497.json, 图片生成/图生图/MiniMax_H3_终极视频生成_多模态+提示词加强_高清加速工作流_2114254930012889090.json, 图片生成/图生图/MiniMax_H3_终极视频生成_多模态+提示词加强_高清加速工作流_2115282881038872577.json, 图片生成/图生图/YZ金鱼-MiniMax H3 终极篇-文武双全_2113256076882825218.json, 平台全量/MiniMax_H3_文戏武戏版＋写提示词_2119663391223668738.json, 视频生成/图生视频/MiniMax H3 终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json, 视频生成/图生视频/MiniMax_H3_含VBVR物理逻辑--终极视频生成_多模态+提示词加强_高清加速工作流_2115965194496208897.json, 视频生成/图生视频/MiniMax_H3_含VBVR物理逻辑--终极视频生成_多模态+提示词加强_高清加速工作流_2115977497996255233.json, 视频生成/视频生视频/MiniMax H3 含VBVR物理逻辑--终极视频生成 （多模态+提示词加强 高清加速工作流）_2111249057271336962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/128.用Minimax H3+360度环绕lora+Skill做动态故事板，动态漫画，高级分镜视频_2109941253944201218.json、图片生成/图生图/H3_终极篇-文武双全短剧-广告通用_2114203657913856001.json、图片生成/图生图/H3_终极篇-文武双全短剧-广告通用_2115242482991722497.json、图片生成/图生图/MiniMax_H3_终极视频生成_多模态+提示词加强_高清加速工作流_2114254930012889090.json、图片生成/图生图/MiniMax_H3_终极视频生成_多模态+提示词加强_高清加速工作流_2115282881038872577.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：48%

## 共有节点

全部 11 个 workflow 都包含：
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
- `BlockSparseAttention` —— 10/11 个有
- `GetNode` —— 10/11 个有
- `GoohaiUniversalSlider` —— 10/11 个有
- `LoadAudio` —— 10/11 个有
- `ModelPreviewOverrideKJ` —— 10/11 个有
- `SetNode` —— 10/11 个有
- `Text` —— 10/11 个有
- `忽略多组孤海` —— 10/11 个有
- `MiniMaxChunkFeedForward` —— 8/11 个有
- `VHS_VideoCombine` —— 8/11 个有
- `LoadVideo` —— 7/11 个有
- `MiniMaxH3PromptEnhancerT8` —— 7/11 个有
- `CM_FloatToInt` —— 6/11 个有
- `GetVideoComponents` —— 6/11 个有
- `ShowAnything|Mie` —— 6/11 个有
- `T8SpeechReference` —— 6/11 个有
- `ZNGB_AudioConcatMulti` —— 6/11 个有
- `CreateVideo` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `SaveVideo` —— 3/11 个有
- `VHS_LoadVideo` —— 3/11 个有
- `SaveImage` —— 2/11 个有
- `Seed (rgthree)` —— 2/11 个有
- `CR Text` —— 1/11 个有
- `ExtendIntermediateSigmas` —— 1/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `ShellAgentPluginOutputText` —— 1/11 个有
- `Vignette` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
