---
name: unknown_workflow_video_upscale_latent_upscale_55
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.889857
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, ManualSigmas, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ModelPreviewOverrideKJ, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3高清打斗_2092544929284317185.json, 视频生成/图生视频/人物跳舞多种舞蹈风格 跳舞自动机-Minimax+H3_2096768052938498049.json, 视频生成/图生视频/人物跳舞多种舞蹈风格+Minimax+H3跳舞自动机_2098950158401761282.json, 视频生成/图生视频/动态壁纸无缝循环(API版)-minimax高质量2k_2093395150411227138.json, 视频生成/图生视频/动态壁纸无缝循环(免费版)-minimax高质量2k_2094661317192937473.json, 视频生成/图生视频/电商广告宣传片-MiniMax H3_2093024927996792834.json, 视频生成/图生视频/跳舞自动机-Minimax H3_2096079611061952513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3高清打斗_2092544929284317185.json、视频生成/图生视频/人物跳舞多种舞蹈风格 跳舞自动机-Minimax+H3_2096768052938498049.json、视频生成/图生视频/人物跳舞多种舞蹈风格+Minimax+H3跳舞自动机_2098950158401761282.json、视频生成/图生视频/动态壁纸无缝循环(API版)-minimax高质量2k_2093395150411227138.json、视频生成/图生视频/动态壁纸无缝循环(免费版)-minimax高质量2k_2094661317192937473.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `ResolutionSelector` —— 5/7 个有
- `CR Prompt Text` —— 3/7 个有
- `DapaoImageAspectRatioResizeNode` —— 2/7 个有
- `DF_Get_image_size` —— 1/7 个有
- `FlashVSR_SM_KSampler` —— 1/7 个有
- `FlashVSR_SM_Model` —— 1/7 个有
- `GetImageRangeFromBatch` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `Text` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `VideoCombineV2` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.81296e+09 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 1.81296e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
