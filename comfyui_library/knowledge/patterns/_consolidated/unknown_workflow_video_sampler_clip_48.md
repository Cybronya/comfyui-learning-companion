---
name: unknown_workflow_video_sampler_clip_48
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.488818
common_nodes: [CLIPLoader, CLIPTextEncode, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, Qwen3_VQA, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/RemixV2+PainterI2V图生视频【动态增强】_1991521193536733186.json, 视频生成/图生视频/RemixV2+PainterI2V图生视频【动态增强】_1992310906843623426.json, 视频生成/图生视频/图生视频（动漫版）_2008911916491608065.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1  6秒视频流 浮云1.19_2013170330788958209.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1图生视频_2008877214103769089.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2009248487199744001.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2063499906979033090.json, 视频生成/图生视频/最强动漫模型DaSiWa8.1视频流_2063503636654813185.json, 视频生成/图生视频/最强动漫视频模型DaSiWa8.1视频流_2009821052431503362.json, 视频生成/图生视频/自动生成动漫视频工作流_2080553179648978945.json, 视频生成/图生视频/首尾帧视频（动漫版）_2008918546440523778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/RemixV2+PainterI2V图生视频【动态增强】_1991521193536733186.json、视频生成/图生视频/RemixV2+PainterI2V图生视频【动态增强】_1992310906843623426.json、视频生成/图生视频/图生视频（动漫版）_2008911916491608065.json、视频生成/图生视频/最强动漫模型DaSiWa8.1  6秒视频流 浮云1.19_2013170330788958209.json、视频生成/图生视频/最强动漫模型DaSiWa8.1图生视频_2008877214103769089.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Int`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PainterI2V` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `INTConstant` —— 9/11 个有
- `RIFE VFI` —— 8/11 个有
- `ShowText|pysssss` —— 8/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `PreviewImage` —— 6/11 个有
- `GetImagesFromBatchIndexed` —— 4/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `DuckHideNode` —— 2/11 个有
- `ImageResizeKJv2` —— 2/11 个有
- `Seed (rgthree)` —— 2/11 个有
- `preview_text` —— 2/11 个有
- `wanBlockSwap` —— 2/11 个有
- `ImageConcatMulti` —— 1/11 个有
- `LoraLoaderModelOnly` —— 1/11 个有
- `WanFirstLastFrameToVideo` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 11 | 82% |
| 采样算法 | 1 | 1 - 1.1 | 11 | 97% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 73% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，11 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1.1，11 个样本，取值集中（一致性 97%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 73%
