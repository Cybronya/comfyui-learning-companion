---
name: unknown_workflow_video_lora_sampler_689
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.41
common_nodes: [BatchImagesNode, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Text, Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetNode, ImageConcatMulti, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, SetNode, TTResolutionSelector, Text Concatenate, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy convertAnything, easy imageScaleDownToSize, easy int, easy seed]
problems: []
missing: []
members: [平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458.json, 平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154.json, 平台全量/sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818.json, 平台全量/贝尔尼尼Bernini 长视频跳舞视频人物替换自用_2068622401906233345.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_689

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458.json、平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154.json、平台全量/sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818.json、平台全量/贝尔尼尼Bernini 长视频跳舞视频人物替换自用_2068622401906233345.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchImagesNode`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageConcatMulti`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `SetNode`
- `TTResolutionSelector`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy convertAnything`
- `easy imageScaleDownToSize`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `ImageFromBatch` —— 2/4 个有
- `VHS_VideoInfoLoaded` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `BerniniPromptEnhancer` —— 1/4 个有
- `CreateVideo` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有
- `SeedVR2ExtraArgs` —— 1/4 个有
- `SeedVR2GGUF` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 4 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，4 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
