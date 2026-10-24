---
name: unknown_workflow_video_lora_sampler_30
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.757385
common_nodes: [CreateCFGScheduleFloatList, JjkText, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/360度旋转-图生视频-wan2.2_1962130657587695617.json, 视频生成/图生视频/576×1024-测试-AI短剧图生视频Wan2.2-14B_1955939150006550529.json, 视频生成/图生视频/720×1280-测试-AI短剧图生视频Wan2.2-14B_1955946689876119554.json, 视频生成/图生视频/AI-Wan2.2-14B 图生视频-极速版_1959887723270189057.json, 视频生成/图生视频/AI站-Wan2.2-14B+图生视频-极速版_1958725154522165249.json, 视频生成/图生视频/CN-Wan2.2-14B 图生视频-极速版_1959809531566043137.json, 视频生成/图生视频/Wan2.2-14B 图生视频 效果炸裂_1976918780821573633.json, 视频生成/图生视频/Wan2.2-14B 图生视频-极速版_1950424438283091970.json, 视频生成/图生视频/Wan2.2-14B 图生视频_1950150331004010497.json, 视频生成/图生视频/Wan2.2-14B 图生视频_1956368575927910401.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2004200391954886657.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2009154616046395394.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2014625691811192833.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2037457877417332737.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2044320478889775106.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2054086706290282498.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2054117320213180418.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2110660986368774146.json, 视频生成/图生视频/Wan2.2-14B 图生视频_高清极速版_1999781370018791426.json, 视频生成/图生视频/Wan2.2-14B+图生视频+高清_2021553233977679873.json, 视频生成/图生视频/图生视频高清版+KJ极速版 Wan2.2 14B 可切换图生视频(升级优化版)_2014248417769295873.json, 视频生成/图生视频/图生视频高清版+KJ极速版 Wan2.2 14B 可切换图生视频(升级优化版)_2080914609724284930.json, 视频生成/图生视频/超高清版图生视频V3_2003625393506689026.json, 视频生成/文生视频/Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337.json, 视频生成/文生视频/Wan2.2图生视频_2010913412934537218.json, 视频生成/文生视频/千问2.5图生视频，极速版_2016217069779427330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_30

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/360度旋转-图生视频-wan2.2_1962130657587695617.json、视频生成/图生视频/576×1024-测试-AI短剧图生视频Wan2.2-14B_1955939150006550529.json、视频生成/图生视频/720×1280-测试-AI短剧图生视频Wan2.2-14B_1955946689876119554.json、视频生成/图生视频/AI-Wan2.2-14B 图生视频-极速版_1959887723270189057.json、视频生成/图生视频/AI站-Wan2.2-14B+图生视频-极速版_1958725154522165249.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 26 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 25/26 个有
- `Int` —— 25/26 个有
- `JWInteger` —— 25/26 个有
- `LoadImage` —— 25/26 个有
- `MathExpression|pysssss` —— 25/26 个有
- `PreviewImage` —— 25/26 个有
- `ImpactSwitch` —— 23/26 个有
- `RH_Captioner` —— 23/26 个有
- `RH_Prompter` —— 23/26 个有
- `RH_Translator` —— 23/26 个有
- `TextCombinerTwo` —— 23/26 个有
- `easy anythingIndexSwitch` —— 23/26 个有
- `easy showAnything` —— 23/26 个有
- `easy cleanGpuUsed` —— 21/26 个有
- `Bjornulf_ShowInt` —— 19/26 个有
- `CR Text Concatenate` —— 19/26 个有
- `CreateVideo` —— 19/26 个有
- `ImageFromBatch+` —— 19/26 个有
- `ImageResizeKJv2` —— 19/26 个有
- `JjkShowText` —— 19/26 个有
- `RH_LLMAPI_NODE` —— 19/26 个有
- `RunningHub ThinkSound` —— 19/26 个有
- `SaveVideo` —— 19/26 个有
- `ShowText` —— 19/26 个有
- `Fast Groups Muter (rgthree)` —— 17/26 个有
- `WanVideoBlockSwap` —— 7/26 个有
- `WanVideoSetBlockSwap` —— 7/26 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/26 个有
- `Anything Everywhere` —— 1/26 个有
- `DF_Integer` —— 1/26 个有
- `Load Image From Url (mtb)` —— 1/26 个有
- `SimpleMath+` —— 1/26 个有
- `String` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
