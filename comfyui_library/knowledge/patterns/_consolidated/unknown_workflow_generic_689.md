---
name: unknown_workflow_generic_689
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.72125
common_nodes: [Bjornulf_ShowInt, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, RH_Captioner, ShowText|pysssss, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/RH批量反推文本可以下载_1958114076587151362.json, 图片生成/反推提示词/lora训练工具之：批量提示词反推（zip上传+for循环+txt文本批量下载）_1964129830243549186.json, 图片生成/反推提示词/图像反推_2084888443162808322.json, 图片生成/反推提示词/图片批量打标反推_1988849488007671810.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_689

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/RH批量反推文本可以下载_1958114076587151362.json、图片生成/反推提示词/lora训练工具之：批量提示词反推（zip上传+for循环+txt文本批量下载）_1964129830243549186.json、图片生成/反推提示词/图像反推_2084888443162808322.json、图片生成/反推提示词/图片批量打标反推_1988849488007671810.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 4 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `RH_Captioner`
- `ShowText|pysssss`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `ShellAgentPluginOutputText` —— 3/4 个有
- `easy saveText` —— 2/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `ToString` —— 1/4 个有
- `easy batchAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
