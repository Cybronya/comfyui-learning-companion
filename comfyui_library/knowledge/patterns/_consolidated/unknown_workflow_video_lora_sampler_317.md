---
name: unknown_workflow_video_lora_sampler_317
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.6485
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_2010362825717325826.json, 视频生成/图生视频/万象+runninghub制作动漫短剧-图生视频工作流（480P横屏）_2038254959346589697.json, 视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流 480P图生视频+V：dxyc2291获取软件_2019552867903868930.json, 视频生成/图生视频/图生视频 自动提示词_2074669211259072514.json, 视频生成/图生视频/图生视频-最强Wan2.2动漫模型DaSiWa_2009346711700901890.json, 视频生成/图生视频/图生视频（6-10秒）自动提示词（动漫特化，写实也很强！）小白上手！_2013233044202721281.json, 视频生成/图生视频/无脑小白上手高画质：图生视频（3-10秒）v2版 更精准_2010920554626293761.json, 视频生成/文生视频/万象+runninghub制作动漫短剧图生视频工作流（480P横屏）+V：50259731获取软件_2002386569740861441.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_317

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/video_wan2_2_14B_i2v_more_motion_2010362825717325826.json、视频生成/图生视频/万象+runninghub制作动漫短剧-图生视频工作流（480P横屏）_2038254959346589697.json、视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流 480P图生视频+V：dxyc2291获取软件_2019552867903868930.json、视频生成/图生视频/图生视频 自动提示词_2074669211259072514.json、视频生成/图生视频/图生视频-最强Wan2.2动漫模型DaSiWa_2009346711700901890.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Int` —— 7/8 个有
- `Text Concatenate` —— 7/8 个有
- `CR Text Replace` —— 6/8 个有
- `PreviewAny` —— 6/8 个有
- `AILab_QwenVL` —— 4/8 个有
- `CFGZeroStar` —— 4/8 个有
- `CR Integer To String` —— 4/8 个有
- `CR Text` —— 4/8 个有
- `ColorMatch` —— 4/8 个有
- `GetAudioDurationFromAudio` —— 4/8 个有
- `JWInteger` —— 4/8 个有
- `LoadAudio` —— 4/8 个有
- `ModelPatchTorchSettings` —— 4/8 个有
- `Text Multiline` —— 4/8 个有
- `WanVideoNAG` —— 4/8 个有
- `wanBlockSwap` —— 4/8 个有
- `Qwen3_VQA` —— 3/8 个有
- `TextInput_` —— 3/8 个有
- `LoadVideo` —— 2/8 个有
- `RHHiddenNodes` —— 1/8 个有
- `Text` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 50% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | lcm | - | 8 | 50% |
| 重绘幅度 | simple | - | 8 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，8 个样本，一致性 50%
- 重绘幅度 最常用 simple，8 个样本，一致性 88%
