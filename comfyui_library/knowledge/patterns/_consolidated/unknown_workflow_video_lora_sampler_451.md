---
name: unknown_workflow_video_lora_sampler_451
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8802
common_nodes: [CLIPVisionLoader, ImageResize+, JWInteger, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Captioner, RH_Translator, TextCombinerTwo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/批次极速图生视频_1946537681393184769.json, 视频生成/图生视频/2039519958744436737.json, 视频生成/图生视频/1943565491653013505.json, 视频生成/图生视频/2023381607255642114.json, 视频生成/文生视频/1952679298441408514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_451

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/批次极速图生视频_1946537681393184769.json、视频生成/图生视频/2039519958744436737.json、视频生成/图生视频/1943565491653013505.json、视频生成/图生视频/2023381607255642114.json、视频生成/文生视频/1952679298441408514.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResize+`
- `JWInteger`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Captioner`
- `RH_Translator`
- `TextCombinerTwo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 4/5 个有
- `LoadImage` —— 3/5 个有
- `Bjornulf_ShowInt` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RHBatchImages:` —— 2/5 个有
- `RHExtractImage` —— 2/5 个有
- `RHUploadZip` —— 2/5 个有
- `easy forLoopEnd` —— 2/5 个有
- `easy forLoopStart` —— 2/5 个有
- `easy imageCount` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
