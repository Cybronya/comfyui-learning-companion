---
name: unknown_workflow_video_sampler_clip_39
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.846833
common_nodes: [CLIPLoader, CLIPTextEncode, ImpactSwitch, KSamplerAdvanced, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_NODE, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1981232802555486209.json, 视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979840137557348353.json, 视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1980202045699428353.json, 视频生成/图生视频/Wan2.2FMLF-3图参考生成连贯视频_1989139978758262786.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_1988842401047392257.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2050784793184481281.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2052282048966082561.json, 视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_2075852358004862978.json, 视频生成/图生视频/Wan_2.2_首中尾三帧视频工作流_1995538932051927042.json, 视频生成/图生视频/【官版】Wan2.2 Moe加速图生视频+智能扩写提示词_1979084209711124482.json, 视频生成/图生视频/【官版】Wan2.2-Lightning4步加速图生视频_1955176719431843842.json, 视频生成/文生视频/Wan2.2 Smooth Mix文生视频（高动态）_1979825054756278274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/WAN2.2-LightX2V-I2V图生视频最强动态搭配_1981232802555486209.json、视频生成/图生视频/Wan2.2 Smooth Mix图生视频（高动态）_1979840137557348353.json、视频生成/图生视频/Wan2.2 Smooth Mix首尾帧视频（高动态）_1980202045699428353.json、视频生成/图生视频/Wan2.2FMLF-3图参考生成连贯视频_1989139978758262786.json、视频生成/图生视频/Wan_2.2_FMLF多帧首尾帧_1988842401047392257.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImpactSwitch`
- `KSamplerAdvanced`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 11/12 个有
- `CLIPVisionLoader` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `LoadImage` —— 11/12 个有
- `Text Concatenate` —— 11/12 个有
- `Wan22PromptSelector` —— 11/12 个有
- `wanBlockSwap` —— 11/12 个有
- `ModelPatchTorchSettings` —— 10/12 个有
- `ImageStitch` —— 9/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `ImageResizeKJv2` —— 8/12 个有
- `ImageBatchMulti` —— 6/12 个有
- `ImageConcatMulti` —— 6/12 个有
- `ImageScaleToTotalPixels` —— 6/12 个有
- `WanMultiFrameRefToVideo` —— 6/12 个有
- `WanImageToVideo` —— 5/12 个有
- `RIFE VFI` —— 2/12 个有
- `ImageConcanate` —— 1/12 个有
- `WanFirstLastFrameToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 92% |
| Prompt 约束强度(CFG) | 7 | 4 - 8 | 12 | 78% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler_ancestral | - | 12 | 83% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 7，观测区间 4 - 8，12 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，12 个样本，一致性 83%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
