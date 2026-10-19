---
name: unknown_workflow_video_clip_unet
type: Unknown Workflow
frequency: 32
level: weak
coverage: 0.8755
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1962917195766534146.json, 视频生成/图生视频/1950878967190454273.json, 视频生成/图生视频/1951086042193571841.json, 视频生成/图生视频/1947906142839144449.json, 视频生成/图生视频/1951893131908337665.json, 视频生成/图生视频/1953037159256289282.json, 视频生成/图生视频/1955442912282775554.json, 视频生成/图生视频/1957271375608213506.json, 视频生成/图生视频/1956923481642426370.json, 视频生成/图生视频/1955447179764797442.json, 视频生成/图生视频/1952614718961848322.json, 视频生成/图生视频/1950000678817193986.json, 视频生成/图生视频/1952550373196279809.json, 视频生成/图生视频/1955912708610772993.json, 视频生成/图生视频/1950367167160213505.json, 视频生成/图生视频/1950070634309181442.json, 视频生成/图生视频/1955832796889714690.json, 视频生成/图生视频/1959200308658384898.json, 视频生成/图生视频/1955505407994183681.json, 视频生成/图生视频/1959201983930511361.json, 视频生成/图生视频/1959202864231034882.json, 视频生成/图生视频/1955506128698445825.json, 视频生成/图生视频/1955448466613813249.json, 视频生成/图生视频/1955834523080691713.json, 视频生成/图生视频/1955835322741526529.json, 视频生成/图生视频/1949713099642294274.json, 视频生成/图生视频/2004402165575806978.json, 视频生成/图生视频/1983463880548655106.json, 视频生成/图生视频/1950029873998905345.json, 视频生成/图生视频/1952552254299680769.json, 视频生成/图生视频/1952551449228185602.json, 视频生成/图生视频/1975460851899568129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（视频生成/图生视频/1962917195766534146.json、视频生成/图生视频/1950878967190454273.json、视频生成/图生视频/1951086042193571841.json、视频生成/图生视频/1947906142839144449.json、视频生成/图生视频/1951893131908337665.json…）

- **类型**：Unknown Workflow
- **样本数**：32
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 32 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 31/32 个有
- `easy ifElse` —— 31/32 个有
- `KSamplerAdvanced` —— 28/32 个有
- `RH_Captioner` —— 27/32 个有
- `easy cleanGpuUsed` —— 23/32 个有
- `easy showAnything` —— 23/32 个有
- `CR Text Replace` —— 22/32 个有
- `LoraLoaderModelOnly` —— 21/32 个有
- `TextBox` —— 21/32 个有
- `LayerUtility: PurgeVRAM V2` —— 16/32 个有
- `LayerUtility: PurgeVRAM` —— 11/32 个有
- `PatchModelPatcherOrder` —— 11/32 个有
- `TorchCompileModelWanVideoV2` —— 11/32 个有
- `ShowText|pysssss` —— 9/32 个有
- `Text Multiline` —— 9/32 个有
- `RH_LLMAPI_NODE` —— 8/32 个有
- `RH_Translator` —— 8/32 个有
- `string_util_StrReplace` —— 8/32 个有
- `INTConstant` —— 4/32 个有
- `KSampler` —— 4/32 个有
- `JjkText` —— 1/32 个有
- `MathExpression|pysssss` —— 1/32 个有
- `Textbox` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 32 | 72% |
| Prompt 约束强度(CFG) | 8 | 1 - 20 | 32 | 42% |
| 采样算法 | 1 | 1 - 4 | 28 | 39% |
| 调度器 | euler | - | 32 | 88% |
| 重绘幅度 | simple | - | 32 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，32 个样本，一致性 72%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 20，32 个样本，取值分散，一致性仅 42%
- 采样算法 中位数 1，观测区间 1 - 4，28 个样本，取值分散，一致性仅 39%
- 调度器 最常用 euler，32 个样本，一致性 88%
- 重绘幅度 最常用 simple，32 个样本，一致性 88%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
