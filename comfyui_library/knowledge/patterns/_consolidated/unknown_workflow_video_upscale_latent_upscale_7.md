---
name: unknown_workflow_video_upscale_latent_upscale_7
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.886087
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, ManualSigmas, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/minimax_h3_r2v_3d_scene_2099337853850443778.json, 平台全量/minimax_h3_r2v_3d_scene_2100403033669726209.json, 平台全量/minimax_h3_r2v_3d_scene_2100491365909090306.json, 平台全量/扣篮的案例_2117999817048813570.json, 平台全量/跳舞全自动生成-Minimax H3_2119017540117684225.json, 视频生成/图生视频/Characters Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+H3+_2104367488405434370.json, 视频生成/图生视频/H3 People Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107279313535062017.json, 视频生成/图生视频/H3+6宫格故事板StoryBoard 生成10~15流畅视频_2093301213247922177.json, 视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107331983230717954.json, 视频生成/图生视频/H3_People_Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+_2107443341985148930.json, 视频生成/图生视频/People+Dancing人物跳舞多种舞蹈风格+跳舞自动机-Minimax+H3+_2110176278711193602.json, 视频生成/图生视频/Videos of People Dancing人物跳舞视频多种舞蹈风格 H3_2100759098823372802.json, 视频生成/图生视频/minimax_h3_r2v_Latent%20Upscaler3_2090611335280287745.json, 视频生成/图生视频/人物跳舞多种舞蹈风格 跳舞自动机-Minimax+H3_2096768052938498049.json, 视频生成/图生视频/人物跳舞多种舞蹈风格+Minimax+H3跳舞自动机_2098950158401761282.json, 视频生成/图生视频/动态壁纸无缝循环(API版)-minimax高质量2k_2093395150411227138.json, 视频生成/图生视频/动态壁纸无缝循环(免费版)-minimax高质量2k_2094661317192937473.json, 视频生成/图生视频/电商广告宣传片-MiniMax H3_2093024927996792834.json, 视频生成/图生视频/跳舞自动机-Minimax H3_2096079611061952513.json, 视频生成/文生视频/动漫短剧工作流（一键直出1080P竖屏短剧提示词未自动优化）_2093587306430160898.json, 视频生成/文生视频/（0825）二采放大1080P12秒-提示词未自动优化_2092123279141195777.json, 视频生成/文生视频/（0826）万象二采放大1080P横屏12秒-提示词未自动优化（增加动态lora）_2092578809114619905.json, 视频生成/文生视频/（0826）万象二采放大1080P竖屏12秒-提示词未自动优化（增加动态lora）_2092617053390856194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_7

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（平台全量/minimax_h3_r2v_3d_scene_2099337853850443778.json、平台全量/minimax_h3_r2v_3d_scene_2100403033669726209.json、平台全量/minimax_h3_r2v_3d_scene_2100491365909090306.json、平台全量/扣篮的案例_2117999817048813570.json、平台全量/跳舞全自动生成-Minimax H3_2119017540117684225.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 22/23 个有
- `MiniMaxH3SigmaShift` —— 22/23 个有
- `ModelPreviewOverrideKJ` —— 22/23 个有
- `SplitSigmas` —— 22/23 个有
- `ResolutionSelector` —— 21/23 个有
- `LoadImage` —— 20/23 个有
- `PrimitiveFloat` —— 20/23 个有
- `RHHiddenNodes` —— 13/23 个有
- `easy showAnything` —— 13/23 个有
- `CR Prompt Text` —— 10/23 个有
- `PrimitiveStringMultiline` —— 10/23 个有
- `INTConstant` —— 4/23 个有
- `VHS_LoadVideo` —— 4/23 个有
- `VHS_VideoInfo` —— 3/23 个有
- `DapaoImageAspectRatioResizeNode` —— 2/23 个有
- `EmptyImage` —— 2/23 个有
- `PreviewImage` —— 2/23 个有
- `easy cleanGpuUsed` —— 2/23 个有
- `ResizeShortestToNode` —— 1/23 个有
- `Text Multiline` —— 1/23 个有
- `easy clearCacheAll` —— 1/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
