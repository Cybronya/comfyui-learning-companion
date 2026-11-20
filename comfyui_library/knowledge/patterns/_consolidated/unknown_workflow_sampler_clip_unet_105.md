---
name: unknown_workflow_sampler_clip_unet_105
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.775167
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, Qwen3_VQA, ShowText|pysssss, TextInput_, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/DaSiWa图生视频（支持18禁_真人_漫画）_2010525636460290050.json, 视频生成/图生视频/DasiWa首尾帧生视频_2030701260868947970.json, 视频生成/图生视频/I2V-丝滑快速首中尾帧图生视频_2037924097656623106.json, 视频生成/图生视频/LightX2V+FMLF首中尾帧三图生视频【动态长视频】_1991681950526160898.json, 视频生成/图生视频/QIANSUI+DaSiWaWAN2.2图生视频（首尾帧）_2008202129441296385.json, 视频生成/图生视频/WAN 万相 最强图生视频  单图  首尾帧  三图首尾帧 短剧生成 AI网剧 动漫视频生成_2015695642802266113.json, 视频生成/图生视频/WAN2.2  最新图生视频 单图 首尾帧 三图首尾帧 万相 短剧生成 AI网剧 动漫视频主角光环_2015990748520390658.json, 视频生成/图生视频/WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2073934911119118338.json, 视频生成/图生视频/WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2073959208336322562.json, 视频生成/图生视频/WAN2.2 DaSiWaV9  最强动漫视频生成（提示词优化版）_2074661334712676354.json, 视频生成/图生视频/WAN2.视频生成（提示词优化版）_2079370650996789249.json, 视频生成/图生视频/wan2.2首帧生视频（附自动生提示词）输出【一段视频 + 尾帧图 + 提示词文本文件】_2015119585170690050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/DaSiWa图生视频（支持18禁_真人_漫画）_2010525636460290050.json、视频生成/图生视频/DasiWa首尾帧生视频_2030701260868947970.json、视频生成/图生视频/I2V-丝滑快速首中尾帧图生视频_2037924097656623106.json、视频生成/图生视频/LightX2V+FMLF首中尾帧三图生视频【动态长视频】_1991681950526160898.json、视频生成/图生视频/QIANSUI+DaSiWaWAN2.2图生视频（首尾帧）_2008202129441296385.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 11/12 个有
- `RIFE VFI` —— 11/12 个有
- `VHS_VideoCombine` —— 11/12 个有
- `ModelSamplingSD3` —— 10/12 个有
- `easy cleanGpuUsed` —— 10/12 个有
- `PreviewImage` —— 9/12 个有
- `WanFirstLastFrameToVideo` —— 9/12 个有
- `ImageBatchMulti` —— 8/12 个有
- `ImageResizeKJv2` —— 8/12 个有
- `PainterI2V` —— 8/12 个有
- `PrimitiveInt` —— 8/12 个有
- `WanMultiFrameRefToVideo` —— 8/12 个有
- `Fast Groups Bypasser (rgthree)` —— 6/12 个有
- `SimpleMath+` —— 6/12 个有
- `LoraLoaderModelOnly` —— 5/12 个有
- `CRTFirstLastFrameSelector` —— 2/12 个有
- `DuckHideNode` —— 2/12 个有
- `GetNode` —— 2/12 个有
- `SaveImage` —— 2/12 个有
- `SetNode` —— 2/12 个有
- `wanBlockSwap` —— 2/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `ImageStitch` —— 1/12 个有
- `MultiplyNode` —— 1/12 个有
- `SDVN Fast Groups Bypasser` —— 1/12 个有
- `ShellAgentPluginOutputText` —— 1/12 个有
- `WanImageToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 50% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 12 | 80% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 100% |
| 重绘幅度 | simple | - | 12 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，12 个样本
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 100%
- 重绘幅度 最常用 simple，12 个样本，一致性 75%
