---
name: unknown_workflow_video_lora_sampler_24
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.753148
common_nodes: [CreateCFGScheduleFloatList, Int, JWInteger, JjkText, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1955939150006550529.json, 视频生成/图生视频/1955946689876119554.json, 视频生成/图生视频/1959887723270189057.json, 视频生成/图生视频/1958725154522165249.json, 视频生成/图生视频/1959809531566043137.json, 视频生成/图生视频/1976918780821573633.json, 视频生成/图生视频/1950424438283091970.json, 视频生成/图生视频/1957628788819554305.json, 视频生成/图生视频/1950150331004010497.json, 视频生成/图生视频/1956368575927910401.json, 视频生成/图生视频/2004200391954886657.json, 视频生成/图生视频/2009154616046395394.json, 视频生成/图生视频/2014625691811192833.json, 视频生成/图生视频/2037457877417332737.json, 视频生成/图生视频/2044320478889775106.json, 视频生成/图生视频/2054086706290282498.json, 视频生成/图生视频/2054117320213180418.json, 视频生成/图生视频/Wan2.2-14B 图生视频_2110660986368774146.json, 视频生成/图生视频/1999781370018791426.json, 视频生成/图生视频/2021553233977679873.json, 视频生成/图生视频/2014248417769295873.json, 视频生成/图生视频/2080914609724284930.json, 视频生成/图生视频/2003625393506689026.json, 视频生成/文生视频/Wan2.2-14B 图生视频RH平台示例工作流_2049013071271694337.json, 视频生成/文生视频/1950150304220274689.json, 视频生成/文生视频/Wan2.2图生视频_2010913412934537218.json, 视频生成/文生视频/千问2.5图生视频，极速版_2016217069779427330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/1955939150006550529.json、视频生成/图生视频/1955946689876119554.json、视频生成/图生视频/1959887723270189057.json、视频生成/图生视频/1958725154522165249.json、视频生成/图生视频/1959809531566043137.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 27 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Int`
- `JWInteger`
- `JjkText`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 26/27 个有
- `PreviewImage` —— 26/27 个有
- `WanVideoImageToVideoEncode` —— 26/27 个有
- `ImpactSwitch` —— 25/27 个有
- `LoadImage` —— 25/27 个有
- `RH_Prompter` —— 25/27 个有
- `TextCombinerTwo` —— 25/27 个有
- `easy showAnything` —— 25/27 个有
- `RH_Captioner` —— 24/27 个有
- `RH_Translator` —— 24/27 个有
- `easy anythingIndexSwitch` —— 24/27 个有
- `easy cleanGpuUsed` —— 21/27 个有
- `Bjornulf_ShowInt` —— 20/27 个有
- `CR Text Concatenate` —— 20/27 个有
- `CreateVideo` —— 20/27 个有
- `ImageFromBatch+` —— 20/27 个有
- `JjkShowText` —— 20/27 个有
- `RH_LLMAPI_NODE` —— 20/27 个有
- `RunningHub ThinkSound` —— 20/27 个有
- `SaveVideo` —— 20/27 个有
- `ShowText` —— 20/27 个有
- `ImageResizeKJv2` —— 19/27 个有
- `Fast Groups Muter (rgthree)` —— 17/27 个有
- `WanVideoBlockSwap` —— 7/27 个有
- `WanVideoSetBlockSwap` —— 6/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/27 个有
- `String` —— 2/27 个有
- `LayerColor: Brightness & Contrast` —— 1/27 个有
- `Load Image From Url (mtb)` —— 1/27 个有
- `WanVideoEmptyEmbeds` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
